import mysql.connector
import os

class psydb():
    def __init__(self):
        db = mysql.connector.connect(
        host = "localhost",
        user = os.ENV.get("mysql_user"),
        password = os.ENV.get("mysql_password"))
        self.cursor = db.cursor()

    def run (self, code):
        return self.cursor.execute(code)
