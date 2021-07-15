from flask import Flask, request
from flask.templating import render_template

from connection.psydb import psydb

from controller.controllers import pacient, psychologist, session

#db = psydb()

app = Flask(__name__)

#@app.route('/psicologo', method = "POST")
#def post(data):
#  try:
#    db.post(data)
#    return 200, "OK"
#  except MYSQL_ERROR:
#    return 400, "Bad Input."
#  except Exception:
#    return 500, f"{Exception}"

@app.route('/')
def home():
  return render_template("home.html")
  
@app.route('/about')
def about():
  return render_template("about.html")

app.run(debug=True)



