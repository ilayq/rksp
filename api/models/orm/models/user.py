from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class UserORM(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    surname = Column(String(20), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    phone_number = Column(String(15), nullable=False, unique=True)
    country = Column(String(64), nullable=False)
    password = Column(String(256), nullable=False)
