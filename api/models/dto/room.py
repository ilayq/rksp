from pydantic import BaseModel
from .user import ExistingUser


class Room(BaseModel):
    room_class_id: int
    room_name: str
    num_rooms: int
    num_guests: int
    area: float
    description: str
    room_amount: int

    @classmethod
    def from_tuple(cls, t: tuple):
        return cls(
            room_class_id=t[0],
            room_name=t[1],
            num_rooms=t[2],
            num_guests=t[3],
            area=t[4],
            description=t[5],
            room_amount=t[6]
        )


class BookingPeriod(BaseModel):
    checkin_timestamp: int
    checkout_timestamp: int


class RoomBooking(BaseModel):
    room: Room
    guest: ExistingUser
    num_guests: int
    period: BookingPeriod
    special_request: str
