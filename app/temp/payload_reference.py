import mysql.connector as sql

conn = sql.connect(
    host="db",   # db will be the alias for docker ip address else localhost
    user="regular",
    password="pass",
    database="employee"
)


def main():
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Employees;")
        # cursor.execute("SELECT EmployeeID, LastName FROM Employees;")
        results = cursor.fetchall()
        out = [dict(zip([key[0] for key in cursor.description], row))
               for row in results]
        print(out, end='')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
