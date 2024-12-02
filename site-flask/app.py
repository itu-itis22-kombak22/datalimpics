from create_database import init_sqlite_db
from insert_datas import insert_db_datas
from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

# Initialize the database and insert data
init_sqlite_db()
insert_db_datas()


def get_db_connection():
    """Establish a connection to the database."""
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn

@app.route("/")
def indexPage():
    """Renders the homepage."""
    return render_template('index.html')

@app.route("/disciplines")
def disciplinesPage():
    """Renders a page displaying all disciplines."""
    conn = get_db_connection()
    disciplines = conn.execute("SELECT * FROM disciplines").fetchall()
    conn.close()
    return render_template('disciplines.html', disciplines=disciplines)

@app.route("/technical_officials")
def technicalOfficialsPage():
    """Renders a page displaying technical officials with additional details."""
    conn = get_db_connection()
    technical_officials = conn.execute("""
        SELECT 
            t.name, 
            t.short_name, 
            t.gender, 
            t.birth_date, 
            c.country_name AS country, 
            t.function, 
            d.discipline_name
        FROM technical_officials t
        JOIN countries c ON t.country = c.country_code
        JOIN disciplines d ON t.discipline_id = d.discipline_id
    """).fetchall()
    conn.close()
    return render_template('technical_officials.html', technical_officials=technical_officials)

@app.route("/medals_total")
def medalsTotalPage():
    """Renders a page displaying medals total data with country names."""
    conn = get_db_connection()
    medals_total = conn.execute("""
        SELECT 
            m.rank, 
            c.country_name, 
            m.gold_medal, 
            m.silver_medal, 
            m.bronze_medal, 
            m.total
        FROM medals_total m
        JOIN countries c ON m.country_code = c.country_code
        ORDER BY m.rank
    """).fetchall()
    conn.close()
    return render_template('medals_total.html', medals_total=medals_total)

@app.route("/countries")
def countriesPage():
    """Renders a page displaying all countries."""
    conn = get_db_connection()
    countries = conn.execute("SELECT * FROM countries").fetchall()
    conn.close()
    return render_template('countries.html', countries=countries)

if __name__ == "__main__":
    app.run(debug=True)



