


import sqlite3

def connect(dbname):
	conn = sqlite3.connect(dbname)

	conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATING TEXT)")

	PRINT("Table created successfully!")

	conn.close()

def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)
    insert_sql = "INSERT INTO OYOY_HOTELS (NAME, ADDRESS, PRICE, AMENITIES, RATING, VALUES (?, ?, ?, ?, ?)"

    conn.execute(insert_sql,values)

    conn.commit()
    conn.close()

def get_hotel_info(dbname):
    conn = sqlite3.connect(dbname)    	