from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

conn = pymysql.connect(
    database = "cbeckford2_socialspread",
    user = "cbeckford2",
    password = "227248309",
    host = "10.100.33.60",
    cursorclass = pymysql.cursors.DictCursor
)

@app.route('/')
def index():
    return render_template('home.html.jinja')

@app.route('/registration', methods = ['GET','POST'])
def registration_page():
    if request.method == 'POST':
        first_name = request.form["first name"]
        last_name = request.form["last name"]
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO `users` (__PUT_COLUMNS_HERE__) VALUES ('{username}', '{password}', '{email}', {first_name}, {last_name})")
        cursor.close()
        conn.commit()
        
    return render_template('registration.html.jinja')

if __name__ == '__main__':
    app.run()
