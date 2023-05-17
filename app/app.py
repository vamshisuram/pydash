from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import subprocess
import json
import time
import logging
import sys

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
app.logger.addHandler(handler)

DB_USER = 'regular'
DB_PASS = 'pass'
DB_NAME = 'employee'
DB_HOST = 'db'  # db will be the alias for docker ip address
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
db = SQLAlchemy(app)


class Employees(db.Model):
    __tablename__ = 'Employees'
    EmployeeID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))

    def __repr__(self):
        return f"EmployeeID: {self.EmployeeID}, FirstName: {self.FirstName}"


@app.route('/hello')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    # app.logger.info('Saying hello to the world')
    print('hello world')
    return 'Hello World'


@app.route('/employees')
def employees():
    results = Employees.query.all()
    for row in results:
        # app.logger.info('employees', row)
        print(row)
    return jsonify('results')


@app.route("/", methods=('GET', 'POST'))
def execute():
    payload = request.get_data(parse_form_data=True)
    content = payload.decode()
    try:
        result = None
        filepath = 'temp/temp' + str(time.time()) + '.py'
        with open(filepath, 'w') as file:
            file.write(content)
        with open(filepath, 'r') as file:
            result = subprocess.run(["python", filepath],
                                    capture_output=True, text=True, check=True)
            response = {"data": json.loads(result.stdout.replace("'", '"'))}
            print("response >>>> \n\n", response)
            return jsonify(response)
    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
