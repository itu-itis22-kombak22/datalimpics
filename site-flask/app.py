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

@app.route("/disciplines", methods=["GET"])
def disciplinesPage():
    """Renders a paginated, searchable, filterable, and sortable page displaying disciplines."""
    conn = get_db_connection()

    # Get query parameters
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Number of disciplines per page
    offset = (page - 1) * per_page
    discipline_name = request.args.get('discipline_name', '').strip()  # Filter by discipline name
    sort_by = request.args.get('sort_by', 'discipline_id')  # Default sorting by ID
    order = request.args.get('order', 'asc')  # Default order ascending

    # Ensure valid sorting column and order
    valid_columns = ['discipline_id', 'discipline_name']
    if sort_by not in valid_columns:
        sort_by = 'discipline_id'
    if order not in ['asc', 'desc']:
        order = 'asc'

    # Base query with optional filtering
    base_query = "SELECT * FROM disciplines"
    filters = []
    params = []

    if discipline_name:
        filters.append("discipline_name LIKE ?")
        params.append(f"%{discipline_name}%")

    if filters:
        base_query += " WHERE " + " AND ".join(filters)

    # Add sorting and pagination
    query = f"{base_query} ORDER BY {sort_by} {order} LIMIT ? OFFSET ?"
    params.extend([per_page, offset])

    disciplines = conn.execute(query, params).fetchall()

    # Count total disciplines for pagination
    count_query = "SELECT COUNT(*) FROM disciplines"
    if filters:
        count_query += " WHERE " + " AND ".join(filters)
    total_disciplines = conn.execute(count_query, params[:-2]).fetchone()[0]

    conn.close()

    # Calculate total pages
    total_pages = (total_disciplines + per_page - 1) // per_page

    return render_template(
        'disciplines.html',
        disciplines=disciplines,
        current_page=page,
        total_pages=total_pages,
        current_discipline_name=discipline_name,
        sort_by=sort_by,
        order=order
    )


@app.route("/add_discipline", methods=["POST"])
def addDiscipline():
    """Add a new discipline."""
    discipline_name = request.form.get("discipline_name")
    conn = get_db_connection()
    conn.execute("INSERT INTO disciplines (discipline_name) VALUES (?)", (discipline_name,))
    conn.commit()
    conn.close()
    return {"message": "Discipline added successfully"}, 201


@app.route("/get_discipline/<int:discipline_id>", methods=["GET"])
def getDiscipline(discipline_id):
    """Fetch a discipline's data by its ID."""
    conn = get_db_connection()
    query = "SELECT discipline_id, discipline_name FROM disciplines WHERE discipline_id = ?"
    discipline = conn.execute(query, (discipline_id,)).fetchone()
    conn.close()

    if discipline:
        return dict(discipline)
    else:
        return {"error": "Discipline not found"}, 404


@app.route("/update_discipline", methods=["POST"])
def updateDiscipline():
    """Update a discipline's details."""
    discipline_id = request.form.get("discipline_id")
    discipline_name = request.form.get("discipline_name")

    conn = get_db_connection()
    conn.execute(
        "UPDATE disciplines SET discipline_name = ? WHERE discipline_id = ?",
        (discipline_name, discipline_id)
    )
    conn.commit()
    conn.close()
    return {"message": "Discipline updated successfully"}, 200


@app.route("/delete_discipline/<int:discipline_id>", methods=["POST"])
def deleteDiscipline(discipline_id):
    """Deletes a discipline."""
    conn = get_db_connection()
    conn.execute("DELETE FROM disciplines WHERE discipline_id = ?", (discipline_id,))
    conn.commit()
    conn.close()

    return {"message": "Discipline deleted successfully"}, 200

@app.route("/technical_officials", methods=["GET"])
def technicalOfficialsPage():
    """Renders a paginated, searchable, filterable, and sortable page displaying technical officials."""
    conn = get_db_connection()

    # Get query parameters
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Number of officials per page
    offset = (page - 1) * per_page
    search = request.args.get('search', '').strip()
    sort_by = request.args.get('sort_by', 'official_id')  # Default sorting by official_id
    order = request.args.get('order', 'asc')  # Default order ascending

    # Ensure valid sorting column and order
    valid_columns = ['official_id', 'name', 'short_name', 'gender', 'birth_date', 'country', 'function', 'discipline_name']
    if sort_by not in valid_columns:
        sort_by = 'name'
    if order not in ['asc', 'desc']:
        order = 'asc'

    # Filters
    gender = request.args.get('gender', '').strip()
    birth_date = request.args.get('birth_date', '').strip()
    country = request.args.get('country', '').strip()
    function = request.args.get('function', '').strip()
    discipline = request.args.get('discipline', '').strip()

    # Base query
    base_query = """
        SELECT 
            t.official_id, 
            t.name, 
            t.short_name, 
            t.gender, 
            t.birth_date, 
            c.country_name AS country, 
            t.function, 
            d.discipline_name
        FROM technical_officials t
        LEFT JOIN countries c ON t.country = c.country_code
        LEFT JOIN disciplines d ON t.discipline_id = d.discipline_id
    """
    filters = []
    params = []

    # Add filters
    if search:
        filters.append("t.name LIKE ?")
        params.append(f"%{search}%")
    if gender:
        filters.append("t.gender = ?")
        params.append(gender)
    if birth_date:
        filters.append("t.birth_date = ?")
        params.append(birth_date)
    if country:
        filters.append("c.country_name LIKE ?")
        params.append(f"%{country}%")
    if function:
        filters.append("t.function LIKE ?")
        params.append(f"%{function}%")
    if discipline:
        filters.append("d.discipline_name LIKE ?")
        params.append(f"%{discipline}%")

    # Apply filters
    if filters:
        base_query += " WHERE " + " AND ".join(filters)

    # Add sorting and pagination
    query = f"{base_query} ORDER BY {sort_by} {order} LIMIT ? OFFSET ?"
    params.extend([per_page, offset])

    # Fetch data
    technical_officials = conn.execute(query, params).fetchall()

    # Count total rows
    count_query = """
        SELECT COUNT(*) 
        FROM technical_officials t
        LEFT JOIN countries c ON t.country = c.country_code
        LEFT JOIN disciplines d ON t.discipline_id = d.discipline_id
    """
    if filters:
        count_query += " WHERE " + " AND ".join(filters)
    total_officials = conn.execute(count_query, params[:-2]).fetchone()[0]

    conn.close()

    # Calculate total pages
    total_pages = (total_officials + per_page - 1) // per_page

    return render_template(
        'technical_officials.html',
        technical_officials=technical_officials,
        current_page=page,
        total_pages=total_pages,
        search_query=search,
        sort_by=sort_by,
        order=order,
        gender=gender,
        birth_date=birth_date,
        country=country,
        function=function,
        discipline=discipline
    )



@app.route("/add_technical_official", methods=["POST"])
def addTechnicalOfficial():
    """Adds a new technical official."""
    name = request.form.get("name")
    short_name = request.form.get("short_name")
    gender = request.form.get("gender")
    birth_date = request.form.get("birth_date")
    country = request.form.get("country")
    function = request.form.get("function")
    discipline_id = request.form.get("discipline_id")

    conn = get_db_connection()
    conn.execute("""
        INSERT INTO technical_officials (name, short_name, gender, birth_date, country, function, discipline_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, short_name, gender, birth_date, country, function, discipline_id))
    conn.commit()
    conn.close()
    return {"message": "Technical official added successfully"}, 201

@app.route("/get_technical_official/<int:official_id>", methods=["GET"])
def getTechnicalOfficial(official_id):
    """Fetch a specific technical official's data."""
    conn = get_db_connection()
    query = """
        SELECT 
            official_id, name, short_name, gender, birth_date, country, function, discipline_id
        FROM technical_officials
        WHERE official_id = ?
    """
    official = conn.execute(query, (official_id,)).fetchone()
    conn.close()
    if official:
        return dict(official)
    else:
        return {"error": "Technical official not found"}, 404

@app.route("/update_technical_official", methods=["POST"])
def updateTechnicalOfficial():
    """Update a technical official's data."""
    official_id = request.form.get("official_id")
    name = request.form.get("name")
    short_name = request.form.get("short_name")
    gender = request.form.get("gender")
    birth_date = request.form.get("birth_date")
    country = request.form.get("country")
    function = request.form.get("function")
    discipline_id = request.form.get("discipline_id")

    conn = get_db_connection()
    conn.execute("""
        UPDATE technical_officials
        SET name = ?, short_name = ?, gender = ?, birth_date = ?, country = ?, function = ?, discipline_id = ?
        WHERE official_id = ?
    """, (name, short_name, gender, birth_date, country, function, discipline_id, official_id))
    conn.commit()
    conn.close()
    return {"message": "Technical official updated successfully"}, 200

@app.route("/delete_technical_official/<int:official_id>", methods=["POST"])
def deleteTechnicalOfficial(official_id):
    """Deletes a technical official."""
    conn = get_db_connection()
    conn.execute("DELETE FROM technical_officials WHERE official_id = ?", (official_id,))
    conn.commit()
    conn.close()
    return {"message": "Technical official deleted successfully"}, 200

@app.route("/search_disciplines", methods=["GET"])
def searchDisciplines():
    """Searches for disciplines."""
    search_term = request.args.get("search_term", "").strip()
    conn = get_db_connection()
    query = """
        SELECT 
            discipline_id, 
            discipline_name
        FROM disciplines
        WHERE discipline_name LIKE ?
    """
    disciplines = conn.execute(query, (f"%{search_term}%",)).fetchall()
    conn.close()
    return render_template(
        'disciplines.html',
        disciplines=disciplines,
        current_page=1,
        total_pages=1,
        search_query=search_term
    )


@app.route("/search_technical_officials", methods=["GET"])
def searchTechnicalOfficials():
    """Searches for technical officials."""
    search_term = request.args.get("search_term", "").strip()
    conn = get_db_connection()
    query = """
        SELECT 
            t.official_id,
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
        WHERE t.name LIKE ?
    """
    technical_officials = conn.execute(query, (f"%{search_term}%",)).fetchall()
    conn.close()
    return render_template(
        'technical_officials.html',
        technical_officials=technical_officials,
        current_page=1,
        total_pages=1,
    )

@app.route("/api/medals_data", methods=["GET"])
def getMedalsData():
    """Return medal statistics for the map."""
    conn = get_db_connection()
    medals_data = conn.execute("""
        SELECT 
            c.country_code AS iso_a3, -- Ensure this matches ISO_A3 codes
            c.country_name,
            m.gold_medal AS gold,
            m.silver_medal AS silver,
            m.bronze_medal AS bronze,
            m.total
        FROM medals_total m
        JOIN countries c ON m.country_code = c.country_code
        ORDER BY m.total DESC
    """).fetchall()
    conn.close()

    # Format the data for the map
    formatted_data = [
        {
            "country_code": row["iso_a3"],
            "country_name": row["country_name"],
            "gold": row["gold"],
            "silver": row["silver"],
            "bronze": row["bronze"],
            "total": row["total"]
        }
        for row in medals_data
    ]

    return {"data": formatted_data}, 200

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
    # 03.12.2024 - The counting function was causing an error because of a syntax in line "conn.execute" I fixed it. -Yigit Alp
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


@app.route("/coaches", methods=["GET"])
def coachesPage():
    """Renders a paginated, searchable, filterable, and sortable page displaying coaches."""
    conn = get_db_connection()

    # Get query parameters
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Number of coaches per page
    offset = (page - 1) * per_page
    search = request.args.get('search', '').strip()
    sort_by = request.args.get('sort_by', 'name')  # Default sorting by name
    order = request.args.get('order', 'asc')  # Default order ascending

    # Ensure valid sorting column and order
    valid_columns = ['name', 'gender', 'birth_date', 'country_code', 'function', 'discipline', 'discipline_name', 'event']
    if sort_by not in valid_columns:
        sort_by = 'name'
    if order not in ['asc', 'desc']:
        order = 'asc'

    # Filters
    gender = request.args.get('gender', '').strip()
    birth_date = request.args.get('birth_date', '').strip()
    country = request.args.get('country', '').strip()
    function = request.args.get('function', '').strip()
    discipline = request.args.get('discipline', '').strip()
    discipline_name = request.args.get('discipline_name', '').strip()
    event = request.args.get('event', '').strip()

    # Base query
    base_query = """
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
    """
    filters = []
    params = []

    # Add filters
    if search:
        filters.append("co.name LIKE ?")
        params.append(f"%{search}%")
    if gender:
        filters.append("co.gender = ?")
        params.append(gender)
    if birth_date:
        filters.append("co.birth_date = ?")
        params.append(birth_date)
    if country:
        filters.append("c.country_name LIKE ?")
        params.append(f"%{country}%")
    if function:
        filters.append("co.function LIKE ?")
        params.append(f"%{function}%")
    if discipline:
        filters.append("co.discipline LIKE ?")
        params.append(f"%{discipline}%")
    if discipline_name:
        filters.append("d.discipline_name LIKE ?")
        params.append(f"%{discipline_name}%")
    if event:
        filters.append("co.event LIKE ?")
        params.append(f"%{event}%")

    # Apply filters
    if filters:
        base_query += " WHERE " + " AND ".join(filters)

    # Add sorting and pagination
    query = f"{base_query} ORDER BY {sort_by} {order} LIMIT ? OFFSET ?"
    params.extend([per_page, offset])

    # Fetch data
    coaches = conn.execute(query, params).fetchall()

    # Count total rows
    count_query = f"SELECT COUNT(*) FROM coaches co LEFT JOIN countries c ON co.country_code = c.country_code LEFT JOIN disciplines d ON co.discipline_id = d.discipline_id"
    if filters:
        count_query += " WHERE " + " AND ".join(filters)

    total_coaches = conn.execute(count_query, params[:-2]).fetchone()[0]
    conn.close()

    # Calculate total pages
    total_pages = (total_coaches + per_page - 1) // per_page

    # Gender dropdown options
    gender_options = {
        "all_selected": "" if not gender else "selected",
        "male_selected": "selected" if gender == "Male" else "",
        "female_selected": "selected" if gender == "Female" else "",
    }

    return render_template(
        'coaches.html',
        coaches=coaches,
        current_page=page,
        total_pages=total_pages,
        search_query=search,
        sort_by=sort_by,
        order=order,
        gender_options=gender_options,
        current_birth_date=birth_date,
        current_country=country,
        current_function=function,
        current_discipline=discipline,
        current_discipline_name=discipline_name,
        current_event=event
    )
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



