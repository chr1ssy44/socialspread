from flask import Flask, render_template, request, redirect
import flask_login
import pymysql
import pymysql.cursors
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.secret_key = "top_secret"

login_manager =flask_login.LoginManager()

login_manager.init_app(app)

auth = HTTPBasicAuth()

class User:
    is_authenticated = True
    is_anonymous = False
    is_active = True

    def __init__(self, id, username, password):
        self.username = username
        self.id = id
        self.password = password

    def get_id(self):

        return str(self.id) 
    
@login_manager.user_loader
def load_user(user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * from `user` WHERE `id` = " + str(user_id))
    result = cursor.fetchone()
    cursor.close()
    conn.commit()

    if result is None:
        
        return None
    
    return User(result['id'], result['username'], result['password'])


conn = pymysql.connect(
    database = "cbeckford2_socialspread",
    user = "cbeckford2",
    password = "227248309",
    host = "10.100.33.60",
    cursorclass = pymysql.cursors.DictCursor
)

@app.route('/')
def index():
    if flask_login.current_user.is_authenticated:
        return redirect('/feed')
    
    return render_template('home.html.jinja')

@app.route('/registration', methods = ['GET','POST'])
def registration_page():
    if request.method == 'POST':
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        username = request.form["username"]
        password = request.form["password"]

        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO `user` (`first_name`, `last_name`, `username`, `password`) VALUES ('{first_name}', '{last_name}', '{username}', '{password}')")
        cursor.close()
        conn.commit()
        
    return render_template('register.html.jinja')

if __name__ == '__main__':
    app.run()

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM `user` WHERE `username` = '{username}'")
        user = cursor.fetchone()
        cursor.close()
        conn.commit()

        if request.form['password'] == user['password']:
            user = load_user(user['id'])

            flask_login.login_user(user)

            return redirect ('/feed')
    
    return render_template('login.html.jinja')

posts =['']

@app.route('/feed', methods = ['GET', 'POST'])
@flask_login.login_required
def post_feed():
    return render_template('feed.html.jinja')

    return flask_login.current_user


 