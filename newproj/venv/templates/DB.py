import sqlite3  
  
con = sqlite3.connect("Database.db")  
print("Database opened successfully")  
  
con.execute("create table productmovement(id INTEGER PRIMARY KEY AUTOINCREMENT,pid INTEGER ,warehouse INTEGER  , qty INTEGER  )")  
# con.execute("insert into product values(1,'mayank',56,'hellow i am mayank')")
con.execute("desc sqlite3")
print("")  
  
con.close()  