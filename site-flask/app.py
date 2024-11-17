from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="datalimpics"
    )
    return connection
@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM coaches")  # Tablonuzun adını doğru yazdığınızdan emin olun
    coaches = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', coaches=coaches)

@app.route('/add', methods=['GET', 'POST'])
def add_coach():
    if request.method == 'POST':
        name = request.form['name']
        short_name = request.form['short_name']
        gender = request.form['gender']
        birth_date = request.form['birth_date']
        country_code = request.form['country_code']
        discipline = request.form['discipline']
        function = request.form['function']
        event = request.form['event']
        url = request.form['url']
        discipline_id = request.form['discipline_id']

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO coaches (name, short_name, gender, birth_date, country_code, discipline, function, event, url, discipline_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (name, short_name, gender, birth_date, country_code, discipline, function, event, url, discipline_id))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('index'))

    return render_template('add_coach.html')

if __name__ == '__main__':
    app.run(debug=True)