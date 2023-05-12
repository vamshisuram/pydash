import mysql.connector as sql

conn = sql.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)


def main():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employees;")
    results = cursor.fetchall()
    print(results)


if __name__ == '__main__':
    main()
