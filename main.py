from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

@app.route('/')
def index():
    return render_template('home.html.jinja')