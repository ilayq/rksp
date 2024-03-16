from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from .models import Base


engine = create_async_engine('sqlite+aiosqlite:///db.db')
session = async_sessionmaker(engine)


async def init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    import asyncio

    asyncio.run(init())
