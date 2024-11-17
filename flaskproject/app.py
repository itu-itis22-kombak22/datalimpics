from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

#veritabanı bağlantısı için
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ada440744",  # Şifre buraya girildi
        database="datalimpics"  # Veritabanı adı buraya girildi
    )
    return connection


@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM athletes")  # Tüm atletleri sql sorugusu ile alma
    athletes = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('athletes.html', athletes=athletes)

if __name__ == '__main__':
    app.run(debug=True)
