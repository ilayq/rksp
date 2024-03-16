import uvicorn
from fastapi import FastAPI
from models.dto.user import UserLogin, UserRegister, ExistingUser
from models.dto.room import RoomBooking, Room, BookingPeriod
from models.dto.status import Status


app = FastAPI()


@app.get('/user')
def user_info(user_id: int) -> ExistingUser:
    ...


@app.post('/user/register')
async def register_user(user_data: UserRegister) -> Status:
    ...


@app.post('/user/login')
async def login_user(user: UserLogin):
    ...


@app.put('/user/update')
async def update_user(user: ExistingUser) -> Status:
    ...


@app.get('/rooms')
async def rooms() -> list[Room]:
    ...


@app.get('/rooms/book')
async def room_book(booking_info: RoomBooking) -> Status:
    ...


@app.get('/rooms/available')
async def rooms_availability(period: BookingPeriod) -> list[Room]:
    ...


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
