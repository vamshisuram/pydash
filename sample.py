import mysql.connector as sql

conn = sql.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM Employees;")
results = cursor.fetchall()
print("results", results)
