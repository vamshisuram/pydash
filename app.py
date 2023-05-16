from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import subprocess
import json
import time

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
            return jsonify(response)
    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
