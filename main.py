import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated

from fastapi.security import OAuth2PasswordRequestForm

from api.models import Status, ExistingUser, UserRegister, Room, RoomBooking, BookingPeriod
from api.auth import get_user,  get_cur_user
from api import encode, make_token
import api.handlers as h


app = FastAPI()


@app.get('/user')
async def user_info(user: Annotated[ExistingUser, Depends(get_cur_user)]) -> ExistingUser | None:
    return await h.user_info(user.id)


@app.post('/user/register')
async def register_user(user_data: UserRegister) -> Status:
    return await h.register_user(user_data)


@app.post('/user/login')
async def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await get_user(form_data.username)
    hashed_pwd = await encode(form_data.password)
    if hashed_pwd != user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": await make_token(user), "token_type": "bearer"}


@app.put('/user/update')
async def update_user(new_user: ExistingUser, user: Annotated[ExistingUser, Depends(get_cur_user)]) -> Status:
    if user.id != new_user.id:
        raise HTTPException(status_code=401, detail="Incorrect id")
    return await h.update_user(new_user)


@app.get('/rooms')
async def rooms() -> list[Room]:
    return await h.get_rooms()


@app.post('/rooms/book')
async def room_book(booking_info: RoomBooking, user: Annotated[ExistingUser, Depends(get_cur_user)]) -> Status:
    return await h.book_room(booking_info, user)


@app.get('/rooms/available')
async def rooms_availability(check_in_timestamp: int, check_out_timestamp: int) -> list[Room]:
    period = BookingPeriod(checkin_timestamp=check_in_timestamp, checkout_timestamp=check_out_timestamp)
    return await h.available_rooms(period)


if __name__ == '__main__':
    uvicorn.run('main:app')
