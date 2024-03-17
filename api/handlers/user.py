from sqlalchemy import select, update
from ..models.orm import UserORM, engine, session
from ..models.dto import UserRegister, Status, StatusEnum, ExistingUser
from ..hashing import encode


async def user_info(user_id: int) -> ExistingUser:
    q = select(UserORM).where(UserORM.id == user_id)
    async with engine.connect() as db:
        user_data = await db.execute(q)
        for user in user_data:
            return ExistingUser.from_tuple(user)


async def register_user(user_data: UserRegister) -> Status:
    user = UserORM(
        name=user_data.name,
        surname=user_data.surname,
        email=user_data.email,
        phone_number=user_data.phone_number,
        country=user_data.country,
        password=await encode(user_data.password)
    )
    try:
        async with session.begin() as db:
            db.add(user)
        return Status(status=StatusEnum.success, comment="")
    except Exception as e:
        print(e)
        return Status(status=StatusEnum.failure, comment="unique restriction violation")


async def update_user(user_data: ExistingUser):
    try:
        q = update(UserORM).where(user_data.id == UserORM.id).values(user_data.dict())
        async with engine.connect() as db:
            await db.execute(q)
            await db.commit()
        return Status(status=StatusEnum.success, comment="")
    except Exception as e:
        return Status(status=StatusEnum.failure, comment=f"{e}")
