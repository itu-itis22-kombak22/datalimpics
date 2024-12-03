from create_database import init_sqlite_db
from insert_datas import insert_db_datas
from flask import Flask, render_template
import sqlite3
app = Flask(__name__)
from flask import Flask, render_template, request
import sqlite3

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

@app.route("/athletes")
def athletesPage():
    """Renders a paginated and filtered page displaying athletes."""
    conn = get_db_connection()

    # Get query parameters
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Number of athletes per page
    offset = (page - 1) * per_page
    filter_name = request.args.get('filter', '').strip()  # Get name filter, trim whitespace
    gender = request.args.get('gender', '').strip()  # Get gender filter

    # Base query
    base_query = """
        SELECT 
            a.name, 
            a.short_name, 
            a.gender, 
            a.birth_date, 
            a.birth_country, 
            a.country,
            a.country_code, 
            a.discipline_code, 
            a.height_mft
        FROM athletes a
    """
    filters = []
    params = []

    #filter
    if filter_name:
        filters.append("a.name LIKE ?")
        params.append(f"%{filter_name}%")
    if gender:
        filters.append("a.gender = ?")
        params.append(gender)

    #filters into query
    if filters:
        base_query += " WHERE " + " AND ".join(filters)

    #pagination from my old work code
    paginated_query = base_query + "LIMIT ? OFFSET?"
    params.extend([per_page, offset])

    # Fetch athletes data
    athletes = conn.execute(paginated_query, params).fetchall()

    # Count total athletes for pagination
    count_query = "SELECT COUNT(*) FROM athletes a"
    if filters:
        count_query += " WHERE " + " AND ".join(filters)
    total_athletes = conn.execute(count_query, params[:-2]).fetchone()[0]

    conn.close()

    # Calculate total pages
    total_pages =(total_athletes + per_page- 1)//per_page

    return render_template(
        'athletes.html',
        athletes=athletes,
        current_page=page,
        total_pages=total_pages,
        current_filter=filter_name,
        current_gender=gender
    )


@app.route("/coaches")
def coachesPage():
    """Renders a page displaying coaches with their country and discipline details."""
    conn = get_db_connection()
    coaches = conn.execute("""
        SELECT 
            co.name, 
            co.short_name, 
            co.gender, 
            co.birth_date, 
            co.country_code, 
            c.country_name AS country, 
            co.function, 
            co.discipline, 
            co.event, 
            d.discipline_name
        FROM coaches co
        LEFT JOIN countries c ON co.country_code = c.country_code
        LEFT JOIN disciplines d ON co.discipline_id = d.discipline_id
    """).fetchall()
    conn.close()
    return render_template('coaches.html', coaches=coaches)

@app.route("/medals")
def medalsPage():
    """Renders a page displaying all medals."""
    conn = get_db_connection()
    medals = conn.execute("""
        SELECT 
            medal_type, 
            medal_code, 
            medal_date, 
            athlete_name, 
            athlete_sex, 
            country_code, 
            discipline_code, 
            event, 
            country, 
            discipline
        FROM medals
    """).fetchall()
    conn.close()
    return render_template('medals.html', medals=medals)

if __name__ == "__main__":
    app.run(debug=True)



