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

@app.route("/countries")
def countriesPage():
    """Renders a paginated, searchable, filterable, and sortable page displaying countries."""
    conn = get_db_connection()

    #query params
    page = request.args.get('page', 1, type=int)
    per_page = 20
    offset = (page - 1) * per_page
    country_name = request.args.get('country_name', '').strip()
    sort_by = request.args.get('sort_by', 'country_code')
    order = request.args.get('order', 'asc')

     # Ensure valid sorting column and order
    valid_columns = ['country_code', 'country_name']
    if sort_by not in valid_columns:
        sort_by = 'country_code'
    if order not in ['asc', 'desc']:
        order = 'asc'

    # Base query with optional filtering
    base_query = "SELECT * FROM countries"
    filters = []
    params = []

    if country_name:
        filters.append("countr_name LIKE ?")
        params.append(f"%{country_name}%")

    if filters:
        base_query += " WHERE " + " AND ".join(filters)

    # Add sorting and pagination
    query = f"{base_query} ORDER BY {sort_by} {order} LIMIT ? OFFSET ?"
    params.extend([per_page, offset])

    countries = conn.execute(query, params).fetchall()

    # Count total country for pagination
    count_query = "SELECT COUNT(*) FROM countries"
    if filters:
        count_query += " WHERE " + " AND ".join(filters)
    total_countries = conn.execute(count_query, params[:-2]).fetchone()[0]

    conn.close()

    total_pages = (total_countries + per_page - 1) // per_page

    return render_template(
        'countries.html',
        countries=countries,
        current_page=page,
        total_pages=total_pages,
        current_country_name=country_name,
        sort_by=sort_by,
        order=order
    )

@app.route("/add_country", methods=["POST"])
def addCountry():
    """Add a new country."""
    country_code = request.form.get("country_code")
    country_name = request.form.get("country_name")
    conn = get_db_connection()
    conn.execute("INSERT INTO countries (country_code, country_name) VALUES (?, ?)", (country_code, country_name))
    conn.commit()
    conn.close()
    return {"message": "Country added successfully"}, 201

@app.route("/get_country/<string:country_code>", methods=["GET"])
def getCountry(country_code):
    """Fetch a country's data by its code."""
    conn = get_db_connection()
    query = "SELECT country_code, country_name FROM countries WHERE country_code = ?"
    country = conn.execute(query, (country_code,)).fetchone()
    conn.close()

    if country:
        return dict(country)
    else:
        return {"error": "Country not found"}, 404
    
@app.route("/update_country", methods=["POST"])
def updateCountry():
    """Update a country's details."""
    country_code = request.form.get("country_code")
    country_name = request.form.get("country_name")

    conn = get_db_connection()
    conn.execute("UPDATE countries SET country_name = ? WHERE country_code = ?", (country_name, country_code))
    conn.commit()
    conn.close()
    return {"message": "Country updated successfully"}, 200

@app.route("/delete_country/<string:country_code>", methods=["POST"])
def deleteCountry(country_code):
    """Deletes a country."""
    conn = get_db_connection()
    conn.execute("DELETE FROM countries WHERE country_code = ?", (country_code,))
    conn.commit()
    conn.close()
    return {"message": "Country deleted successfully"}, 200

@app.route("/search_countries", methods=["GET"])
def searchCountries():
    """Searches for countries."""
    search_term = request.args.get("search_term", "").strip()
    conn = get_db_connection()
    query = """
        SELECT 
            country_code, 
            country_name
        FROM countries
        WHERE country_name LIKE ?
    """
    countries = conn.execute(query, (f"%{search_term}%",)).fetchall()
    conn.close()
    return render_template(
        'countries.html',
        countries=countries,
        current_page=1,
        total_pages=1,
        search_query=search_term
    )



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

@app.route("/medals_total", methods=["GET"])
def medalsTotalPage():
    """Renders a page displaying medals total data with country names."""
    conn = get_db_connection()

    page = request.args.get('page', 1, type=int)
    per_page = 20
    offset = (page - 1) * per_page
    search = request.args.get('search', '').strip()
    sort_by = request.args.get('sort_by', 'rank')
    order = request.args.get('order', 'asc')

    valid_columns = ['rank', 'country_name', 'gold_medal', 'silver_medal', 'bronze_medal', 'total', 'country_code']
    if sort_by not in valid_columns:
        sort_by = 'rank'
    if order not in ['asc', 'desc']:
        order = 'asc'

        
    rank = request.args.get('rank', '').strip()
    country_name = request.args.get('country_name', '').strip()
    gold_medal = request.args.get('gold_medal', '').strip()
    silver_medal = request.args.get('silver_medal', '').strip()
    bronze_medal = request.args.get('bronze_medal', '').strip()
    total_medal = request.args.get('total_medal', '').strip()
    country_code = request.args.get('country_code', '').strip()

    base_query = """
        SELECT
            m.rank,
            c.country_name,
            m.gold_medal,
            m.silver_medal,
            m.bronze_medal,
            m.total,
            m.country_code
        FROM medals_total m
        JOIN countries c ON m.country_code = c.country_code
    """
    filters = []
    params = []

    if search:
        filters.append("c.country_name LIKE ?")
        params.append(f"%{search}%")
    if rank:
        filters.append("m.rank = ?")
        params.append(rank)
    if country_name:
        filters.append("c.country_name LIKE ?")
        params.append(f"%{country_name}%")
    if gold_medal:
        filters.append("m.gold_medal = ?")
        params.append(gold_medal)
    if silver_medal:
        filters.append("m.silver_medal = ?")
        params.append(silver_medal)
    if bronze_medal:
        filters.append("m.bronze_medal = ?")
        params.append(bronze_medal)
    if total_medal:
        filters.append("m.total = ?")
        params.append(total_medal)
    if country_code:
        filters.append("m.country_code = ?")
        params.append(country_code)

    if filters:
        base_query += " WHERE " + " AND ".join(filters)

    query = f"{base_query} ORDER BY {sort_by} {order} LIMIT ? OFFSET ?"
    params.extend([per_page, offset])

    medals_total = conn.execute(query, params).fetchall()

    count_query = "SELECT COUNT(*) FROM medals_total m JOIN countries c ON m.country_code = c.country_code"
    if filters:
        count_query += " WHERE " + " AND ".join(filters)
    total_medals = conn.execute(count_query, params[:-2]).fetchone()[0]

    conn.close()

    total_pages = (total_medals + per_page - 1) // per_page

    return render_template(
        'medals_total.html',
        medals_total=medals_total,
        current_page=page,
        total_pages=total_pages,
        search_query=search,
        sort_by=sort_by,
        order=order,
        rank=rank,
        country_name=country_name,
        gold_medal=gold_medal,
        silver_medal=silver_medal,
        bronze_medal=bronze_medal,
        total_medal=total_medal,
        country_code=country_code
    )



@app.route("/add_medals_total", methods=["POST"])
def addMedalsTotal():
    """Adds a new entry to the medals_total table."""
    rank = request.form.get("rank", type=int)
    country_code = request.form.get("countryCode")
    gold_medal = request.form.get("goldMedal", type=int)
    silver_medal = request.form.get("silverMedal", type=int)
    bronze_medal = request.form.get("bronzeMedal", type=int)
    total = gold_medal + silver_medal + bronze_medal

    conn = get_db_connection()

    # Check if the country code exists
    country_exists = conn.execute("SELECT 1 FROM countries WHERE country_code = ?", (country_code,)).fetchone()
    if not country_exists:
        conn.close()
        return {"message": "Country code does not exist"}, 404
    # Check if the medals total entry already exists
    medals_total_exists = conn.execute("SELECT 1 FROM medals_total WHERE country_code = ?", (country_code,)).fetchone()
    if medals_total_exists:
        conn.close()
        return {"message": "Medals total entry already exists for this country"}, 409

    conn.execute(
        """
        INSERT INTO medals_total (rank, country_code, gold_medal, silver_medal, bronze_medal, total)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (rank, country_code, gold_medal, silver_medal, bronze_medal, total)
    )
    conn.commit()
    conn.close()
    return {"message": "Medals total added successfully"}, 201

@app.route("/get_medals_total/<string:country_code>", methods=["GET"])
def getMedalsTotal(country_code):
    """Fetches a medals total entry by country code."""
    conn = get_db_connection()
    query = "SELECT * FROM medals_total WHERE country_code = ?"
    medals_total = conn.execute(query, (country_code,)).fetchone()
    conn.close()

    if medals_total:
        return dict(medals_total)
    else:
        return {"error": "Medals total entry not found"}, 404

@app.route("/update_medals_total", methods=["POST"])
def updateMedalsTotal():
    """Updates an existing medals total entry."""
    country_code = request.form.get("country_code", type=str)
    rank = request.form.get("rank", type=int)
    gold_medal = request.form.get("gold_medal", type=int)
    silver_medal = request.form.get("silver_medal", type=int)
    bronze_medal = request.form.get("bronze_medal", type=int)
    total = gold_medal + silver_medal + bronze_medal

    conn = get_db_connection()
    conn.execute(
        """
        UPDATE medals_total
        SET rank = ?, gold_medal = ?, silver_medal = ?, bronze_medal = ?, total = ?
        WHERE country_code = ?
        """,
        (rank, gold_medal, silver_medal, bronze_medal, total, country_code)
    )
    conn.commit()
    conn.close()
    return {"message": "Medals total updated successfully"}, 200

@app.route("/delete_medals_total/<string:country_code>", methods=["POST"])
def deleteMedalsTotal(country_code):
    """Deletes a medals total entry."""
    conn = get_db_connection()
    conn.execute("DELETE FROM medals_total WHERE country_code = ?", (country_code,))
    conn.commit()
    conn.close()
    return {"message": "Medals total deleted successfully"}, 200

@app.route("/search_medals_total", methods=["GET"])
def searchMedalsTotal():
    """Searches for medals total entries by country name."""
    search_term = request.args.get("search_term", "").strip()
    conn = get_db_connection()
    query = """
        SELECT m.*, c.country_name
        FROM medals_total m
        JOIN countries c ON m.country_code = c.country_code
        WHERE c.country_name LIKE ?
    """
    medals_totals = conn.execute(query, (f"%{search_term}%",)).fetchall()
    conn.close()

    return render_template(
        'medals_total.html',
        medals_total=medals_totals,
        current_page=1,
        total_pages=1,
        search_query=search_term
    )

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
    conn = get_db_connection()

    # Get query parameters
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Number of coaches per page
    offset = (page - 1) * per_page
    search = request.args.get('search', '').strip()
    sort_by = request.args.get('sort_by', 'coach_id')  # Default sorting by ID
    order = request.args.get('order', 'asc')  # Default order ascending

    # Ensure valid sorting column and order
    valid_columns = ['coach_id', 'name', 'short_name', 'gender', 'birth_date', 'country_code', 'function', 'discipline', 'event']
    if sort_by not in valid_columns:
        sort_by = 'coach_id'
    if order not in ['asc', 'desc']:
        order = 'asc'

    # Base query with optional filtering
    base_query = "SELECT * FROM coaches"
    filters = []
    params = []

    if search:
        filters.append("name LIKE ?")
        params.append(f"%{search}%")

    if filters:
        base_query += " WHERE " + " AND ".join(filters)

    # Add sorting and pagination
    query = f"{base_query} ORDER BY {sort_by} {order} LIMIT ? OFFSET ?"
    params.extend([per_page, offset])

    coaches = conn.execute(query, params).fetchall()

    # Count total coaches for pagination
    count_query = "SELECT COUNT(*) FROM coaches"
    if filters:
        count_query += " WHERE " + " AND ".join(filters)
    total_coaches = conn.execute(count_query, params[:-2]).fetchone()[0]

    conn.close()

    # Calculate total pages
    total_pages = (total_coaches + per_page - 1) // per_page

    return render_template(
        'coaches.html',
        coaches=coaches,
        current_page=page,
        total_pages=total_pages,
        search_query=search,
        sort_by=sort_by,
        order=order
    )


@app.route("/add_coach", methods=["POST"])
def addCoach():
    name = request.form.get("name")
    short_name = request.form.get("short_name")
    gender = request.form.get("gender")
    birth_date = request.form.get("birth_date")
    country_code = request.form.get("country_code")
    function = request.form.get("function")
    discipline = request.form.get("discipline")
    event = request.form.get("event")

    if name and gender and birth_date and country_code:
        conn = get_db_connection()
        conn.execute("""
            INSERT INTO coaches (name, short_name, gender, birth_date, country_code, function, discipline, event)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, short_name, gender, birth_date, country_code, function, discipline, event))
        conn.commit()
        conn.close()
        return {"message": "Coach added successfully"}, 201
    else:
        return {"error": "Required fields are missing"}, 400


@app.route("/get_coach/<int:coach_id>", methods=["GET"])
def getCoach(coach_id):
    conn = get_db_connection()
    query = "SELECT * FROM coaches WHERE coach_id = ?"
    coach = conn.execute(query, (coach_id,)).fetchone()
    conn.close()

    if coach:
        return dict(coach), 200
    else:
        return {"error": "Coach not found"}, 404


@app.route("/update_coach", methods=["POST"])
def updateCoach():
    coach_id = request.form.get("coach_id")
    name = request.form.get("name")
    short_name = request.form.get("short_name")
    gender = request.form.get("gender")
    birth_date = request.form.get("birth_date")
    country_code = request.form.get("country_code")
    function = request.form.get("function")
    discipline = request.form.get("discipline")
    event = request.form.get("event")

    if coach_id:
        conn = get_db_connection()
        conn.execute("""
            UPDATE coaches
            SET name = ?, short_name = ?, gender = ?, birth_date = ?, country_code = ?, function = ?, discipline = ?, event = ?
            WHERE coach_id = ?
        """, (name, short_name, gender, birth_date, country_code, function, discipline, event, coach_id))
        conn.commit()
        conn.close()
        return {"message": "Coach updated successfully"}, 200
    else:
        return {"error": "Coach ID is required"}, 400


@app.route("/delete_coach/<int:coach_id>", methods=["POST"])
def deleteCoach(coach_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM coaches WHERE coach_id = ?", (coach_id,))
    conn.commit()
    conn.close()

    return {"message": "Coach deleted successfully"}, 200


@app.route("/edit_coach/<int:coach_id>", methods=["POST"])
def editCoach(coach_id):
    conn = get_db_connection()
    query = "SELECT * FROM coaches WHERE coach_id = ?"
    coach = conn.execute(query, (coach_id,)).fetchone()
    conn.close()

    if coach:
        return {"coach": dict(coach)}, 200
    else:
        return {"error": "Coach not found"}, 404



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



