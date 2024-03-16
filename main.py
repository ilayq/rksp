import uvicorn
from fastapi import FastAPI
from api.models import Status, ExistingUser, UserRegister, UserLogin, Room, RoomBooking, BookingPeriod
import api.handlers as h


app = FastAPI()


@app.get('/user')
async def user_info(user_id: int) -> ExistingUser:
    return await h.user_info(user_id)


@app.post('/user/register')
async def register_user(user_data: UserRegister) -> Status:
    return await h.register_user(user_data)


@app.post('/user/login')
async def login_user(user: UserLogin):
    ...


@app.put('/user/update')
async def update_user(user: ExistingUser) -> Status:
    return await h.update_user(user)


@app.get('/rooms')
async def rooms() -> list[Room]:
    return await h.get_rooms()


@app.post('/rooms/book')
async def room_book(booking_info: RoomBooking) -> Status:
    return await h.book_room(booking_info)


@app.get('/rooms/available')
async def rooms_availability(check_in_timestamp: int, check_out_timestamp: int) -> list[Room]:
    period = BookingPeriod(checkin_timestamp=check_in_timestamp, checkout_timestamp=check_out_timestamp)
    return await h.available_rooms(period)


if __name__ == '__main__':
    uvicorn.run('main:app')
