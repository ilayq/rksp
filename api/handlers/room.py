from .. import ExistingUser
from ..models import Room, Status, RoomBooking, BookingPeriod, StatusEnum
from ..models import RoomORM, BookingORM as BookingORM

from ..models import engine, session

from sqlalchemy import select, and_, or_


async def get_rooms() -> list[RoomORM]:
    q = select(RoomORM)
    rooms = []
    async with engine.connect() as db:
        for t in await db.execute(q):
            rooms.append(Room.from_tuple(t))
    return rooms


async def book_room(data: RoomBooking, user: ExistingUser) -> Status:
    available = await available_rooms(data.period)
    available = [room.room_class_id for room in available]
    if data.room.room_class_id not in available:
        return Status(status=StatusEnum.failure, comment="no available rooms")
    try:
        async with session.begin() as db:
            orm = BookingORM(
                room_type=data.room.room_class_id,
                user_id=user.id,
                guests_num=data.num_guests,
                check_in=data.period.checkin_timestamp,
                check_out=data.period.checkout_timestamp,
                special_request=data.special_request
            )
            db.add(orm)
        async with engine.connect() as db:
            q = select(BookingORM.id).order_by(-BookingORM.id)
            for id_ in await db.execute(q):
                return Status(status=StatusEnum.success, comment=f"{id_[0]}")
    except Exception as e:
        return Status(status=StatusEnum.failure, comment=f"{e}")


async def available_rooms(period: BookingPeriod) -> list[Room]:
    all_rooms = select(RoomORM)
    res = []
    async with engine.connect() as db:
        for room in await db.execute(all_rooms):
            r = Room.from_tuple(room)
            bookings_in_period = select(BookingORM).where(and_(
                BookingORM.room_type == r.room_class_id,
                or_(
                    and_(period.checkin_timestamp <= BookingORM.check_in, BookingORM.check_in < period.checkout_timestamp),
                    and_(period.checkin_timestamp < BookingORM.check_out, BookingORM.check_out <= period.checkout_timestamp)
                )
            ))
            lst = await db.execute(bookings_in_period)
            bookings = len(list(lst))
            if r.room_amount > bookings:
                res.append(r)
    return res
