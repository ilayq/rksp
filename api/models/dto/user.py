from pydantic import BaseModel


class BaseUser(BaseModel):
    name: str
    surname: str
    phone_number: str
    email: str
    country: str


class UserRegister(BaseUser):
    password: str


class ExistingUser(BaseUser):
    id: int
    password: str


    @classmethod
    def from_tuple(cls, t: tuple):
        return cls(
            id=t[0],
            name=t[1],
            surname=t[2],
            email=t[3],
            phone_number=t[4],
            country=t[5],
            password=t[6],
        )
