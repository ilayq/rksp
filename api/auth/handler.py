from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from ..models import engine, ExistingUser, UserORM
from ..handlers import user_info
from ..hashing import decode_token

from sqlalchemy import select


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")


async def is_email(username: str) -> bool:
    # TODO
    return True


async def is_phone_number(username: str) -> bool:
    # TODO
    return True


async def get_user(username: str) -> ExistingUser:
    if await is_email(username):
        query_param = UserORM.email
    elif await is_phone_number(username):
        query_param = UserORM.phone_number
    else:
        raise Exception("Wrong email/phone_number")

    q = select(UserORM.id).where(query_param == username)
    async with engine.connect() as db:
        res = await db.execute(q)
        for user in res:
            if not user:
                raise Exception("Wrong email/phone_number")
            return await user_info(user[0])


async def get_cur_user(token: Annotated[str, Depends(oauth2_scheme)]):
    return await decode_token(token)
