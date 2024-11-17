
from flask import Flask 
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from create_database import init_sqlite_db
from insert_datas import insert_db_datas


app = Flask(__name__)


init_sqlite_db()

insert_db_datas()

def get_data_from_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medals_total")
    medals_total = cursor.fetchall()
    print("Medals Total:", medals_total)

    cursor.execute("SELECT * FROM countries")
    countries = cursor.fetchall()
    print("Countries:", countries)

    conn.close()

#get_data_from_db()
@app.route("/")
def indexPage():
    return render_template('index.html')