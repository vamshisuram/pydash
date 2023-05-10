from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

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

    def as_dict(self):
        return {'EmployeeID': self.EmployeeID, 'FirstName': self.FirstName}


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/execute")
def execute():
    employees = Employees.query.all()
    return jsonify([employee.as_dict() for employee in employees])


if __name__ == '__main__':
    app.run()
