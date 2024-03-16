from sqlalchemy import Column, Integer, String, Float
from .user import Base


class RoomORM(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_name = Column(String(20), nullable=False)
    num_rooms = Column(Integer, nullable=False)
    num_guests = Column(Integer, nullable=False)
    area = Column(Float, nullable=False)
    description = Column(String(4096), nullable=False)
    room_amount = Column(Integer, nullable=False)
