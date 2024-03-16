from enum import Enum
from pydantic import BaseModel


class StatusEnum(Enum):
    success = 1
    failure = 0


class Status(BaseModel):
    status: StatusEnum
    comment: str
