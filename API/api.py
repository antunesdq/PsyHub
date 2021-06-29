from flask import Flask
from flask_restx import fields, Api, Resource

import mysql.connector

app = Flask(__name__)

api = Api(app)



db = database()

@app.route('/psicologo', method = "POST")
def post(data):
  try:
    db.post(data)
    return 200, "OK"
  except MYSQL_ERROR:
    return 400, "Bad Input."
  except Exception:
    return 500, f"{Exception}"
 
app.run(debug=False)