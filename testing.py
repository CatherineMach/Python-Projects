
import sqlite3
connection = sqlite3.connect("C:\Users\flowe\Documents\GitHub\Python-Projects/test_database.db")

c = connection.cursor()

c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT")


