import sqlite3

connection = sqlite3.connect("items.db")
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)"
connection.execute(create_table)

connection.commit()
connection.close()