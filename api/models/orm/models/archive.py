from sqlalchemy import Column, Integer, String, ForeignKey
from .booking import Base


class BookingArchiveORM(Base):
    __tablename__ = 'booking_archive'

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_type = Column(Integer, ForeignKey('rooms.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    guests_num = Column(Integer, nullable=False)
    check_in = Column(Integer, nullable=False)
    check_out = Column(Integer, nullable=False)
    special_request = Column(String(4096))
