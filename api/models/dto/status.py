from enum import Enum
from pydantic import BaseModel
from typing import Union


class StatusEnum(Enum):
    success = 1
    failure = 0


class Status(BaseModel):
    status: StatusEnum
    comment: Union[str, None]
