from flask import (Flask, g, redirect, render_template, request, session, url_for)

from connection.psydb import psydb

from controller.controllers import pacient, psychologist, psi_session

#db = psydb()
class User():
    def __init__(self, name, password, id):
        self.name = name
        self.id = id
        self.password = password

users = []
users.append(User('matt', 'pwd', 1))

app = Flask(__name__)
app.secret_key = 'whatever'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = users[0]
        g.user = user

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        pwd = request.form['password']
        if username in users.keys() and users['user'] ==  pwd:
            session['user_id'] = username
            return redirect(url_for('profile'))
        else:
            return redirect(url_for("home"))

    return render_template("home.html")
  

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('home'))

    return render_template('profile.html')


@app.route('/about')
def about():
  return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)