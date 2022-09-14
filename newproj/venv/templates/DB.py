import sqlite3  
  
con = sqlite3.connect("Database.db")  
print("Database opened successfully")  
  
con.execute("create table location(id INTEGER PRIMARY KEY AUTOINCREMENT,location text NOT NULL )")  
# con.execute("insert into product values(1,'mayank',56,'hellow i am mayank')")
print("Table created successfully")  
  
con.close()  