from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

conn = pymysql.connect(
    database = "cbeckford2_todos",
    user = "cbeckford2",
    password = "227248309",
    host = "10.100.33.60",
    cursorclass = pymysql.cursors.DictCursor
)