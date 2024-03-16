from pydantic import BaseModel
from .user import ExistingUser


class Room(BaseModel):
    room_class_id: int
    num_rooms: int
    num_guests: int
    area: float
    description: str


class BookingPeriod(BaseModel):
    checkin_timestamp: int
    checkout_timestamp: int


class RoomBooking(BaseModel):
    room: Room
    guest: ExistingUser
    num_guests: int
    period: BookingPeriod
    special_request: str
