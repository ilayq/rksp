from api.models.orm import engine, Base
from sqlite3 import connect


async def init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    con = connect("db.db")
    cur = con.cursor()
    cur.execute("insert into rooms(room_name, num_rooms, num_guests, area, description, room_amount)\
                values ('lux', 2, 2, 20, 'super room', 2)")

    con.commit()
    con.close()


if __name__ == '__main__':
    import asyncio

    asyncio.run(init())
