import sqlite3
def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")
    conn.execute('DROP TABLE IF EXISTS medals_total')
    conn.execute('''
        CREATE TABLE medals_total (
            Rank INTEGER NOT NULL,
            Country_Code TEXT NOT NULL,
            Gold_Medal INTEGER DEFAULT NULL,
            Silver_Medal INTEGER DEFAULT NULL,
            Bronze_Medal INTEGER DEFAULT NULL,
            Total INTEGER DEFAULT NULL,
            Country TEXT,
            PRIMARY KEY (Country_Code, Rank),
            FOREIGN KEY (Country_Code) REFERENCES countries (country_code)
        )
    ''')
    print("medals_total table created successfully")
    conn.execute('DROP TABLE IF EXISTS countries')
    conn.execute('''
        CREATE TABLE countries (
            country_code TEXT NOT NULL,
            country_name TEXT DEFAULT NULL,
            PRIMARY KEY (country_code)
        )
    ''')
    print("countries table created successfully")
    conn.close()
    # Only drop and create new tables

    conn.execute('DROP TABLE IF EXISTS disciplines')

    # Create the disciplines table
    conn.execute('''
        CREATE TABLE disciplines (
            discipline_id INTEGER PRIMARY KEY AUTOINCREMENT,
            discipline_name TEXT NOT NULL UNIQUE
        )
    ''')
    print("disciplines table created successfully")
    conn.execute('DROP TABLE IF EXISTS technical_officials')
    # Create the technical_officials table
    conn.execute('''
        CREATE TABLE technical_officials (
            `name` TEXT,
            `short_name` TEXT,
            `gender` TEXT,
            `birth_date` TEXT,
            `country` varchar(30) DEFAULT NULL,
            `function` TEXT,
            discipline_id INTEGER NOT NULL,
            official_id INTEGER PRIMARY KEY AUTOINCREMENT,
            FOREIGN KEY (country) REFERENCES countries (country_code),
            FOREIGN KEY (discipline_id) REFERENCES disciplines (discipline_id)
        )
    ''')
    print("technical_officials table created successfully")

    conn.close()
