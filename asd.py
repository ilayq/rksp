from sqlite3 import connect


con = connect('db.db')
cur = con.cursor()
cur.execute("insert into rooms(room_name, num_rooms, num_guests, area, description, room_amount) values ('lux', 2, 2, 20, 'super room', 10);")
con.commit()
con.close()