from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
DB_USER = 'root'
DB_PASS = ''
DB_NAME = 'employee'
DB_HOST = 'localhost'
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
db = SQLAlchemy(app)


class Employees(db.Model):
    __tablename__ = 'Employees'
    EmployeeID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))

    def __str__(self):
        # return json.dumps(dict(self), ensure_ascii=False)
        return f'EmployeeID: {self.EmployeeID}, FirstName: {self.FirstName}'


@app.route("/", methods=('GET', 'POST'))
def execute():
    # employees = Employees.query.all()
    # return jsonify([employee.as_dict() for employee in employees])
    payload = request.get_data(parse_form_data=True)
    print('payload', payload)

    # parse and evaluate the script
    # invoke subprocess and take results
    exec(payload.decode())

    statement = '''
      SELECT * FROM Employees;
    '''
    with db.engine.connect() as conn:
        results = conn.execute(text(statement)).fetchall()
        results = [tuple(row) for row in results]
        # results = [tuple(row) for row in results]
    return jsonify(dict(data=results))    # data contains dataframe!


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
