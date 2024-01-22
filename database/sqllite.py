import sqlite3;
connection = sqlite3.connect("local_database.db");
cursor = connection.cursor();
datas = "";
#query = "CREATE TABLE my_table (id integer primary key autoincrement, name varchar(20));";

#query = "SELECT * from my_table"

#query = """INSERT INTO my_table (name) VALUES """
#datas = "('ramesh'),('hari')"

#cursor.execute(query+datas);
#connection.commit();
""""
rows = cursor.fetchall()
for row in rows:
    print(row)
"""
cursor.close();
connection.close();