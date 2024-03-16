from pydantic import BaseModel


class BaseUser(BaseModel):
    name: str
    surname: str
    phone: str
    email: str
    country: str


class UserLogin(BaseModel):
    login: str
    password: str


class UserRegister(BaseUser):
    pass


class ExistingUser(BaseUser):
    id: int
