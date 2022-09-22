import sqlite3 

connection = sqlite3.connect("data.db") # it will store data in data.db file 

cursor = connection.cursor() #cursor is used to execute the sql commands

create_table = "CREATE TABLE users(id int,username text,password text)"
cursor.execute(create_table)

user = (1,'Anna','ana123')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query,user)


# insert multiple records
multipleUser = [
    (2,'Nikki','n987'),
    (2,'golu','gol')
]

insert_many = "INSERT INTO users VALUES (?,?,?)"
cursor.executemany(insert_many,multipleUser)

# select records
selectQuery = "SELECT * FROM users"
for row in cursor.execute(selectQuery):
    print(row)

connection.commit() # to save all the changes
connection.close()

# delete the data.db file if exist before creating again 