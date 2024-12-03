import sqlite3

def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    # Only drop and create new tables
    conn.execute('DROP TABLE IF EXISTS technical_officials')
    conn.execute('DROP TABLE IF EXISTS disciplines')

    # Create the disciplines table
    conn.execute('''
        CREATE TABLE disciplines (
            discipline_id INTEGER PRIMARY KEY AUTOINCREMENT,
            discipline_name TEXT NOT NULL UNIQUE
        )
    ''')
    print("disciplines table created successfully")

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

    conn.execute('''
    CREATE TABLE IF NOT EXISTS athletes (
        name TEXT,
        short_name TEXT,
        gender TEXT,
        birth_date TEXT,
        birth_country TEXT,
        country TEXT,
        country_code VARCHAR(10) DEFAULT NULL,
        discipline_code TEXT,
        height_mft TEXT,
        athlete_id INTEGER NOT NULL AUTO_INCREMENT,
        discipline_id INTEGER DEFAULT NULL,
        PRIMARY KEY (athlete_id),
        KEY fk_athlete_country (country_code),
        KEY fk_athletes_disciplines (discipline_id),
        CONSTRAINT fk_athlete_country FOREIGN KEY (country_code) REFERENCES countries (country_code),
        CONSTRAINT fk_athletes_disciplines FOREIGN KEY (discipline_id) REFERENCES disciplines (discipline_id)
    )
    ''')
    print("athletes table created successfully")

    conn.execute('''
    DROP TABLE IF EXISTS coaches;

    CREATE TABLE coaches (
        name TEXT,
        short_name TEXT,
        gender TEXT,
        birth_date TEXT,
        country_code VARCHAR(10) DEFAULT NULL,
        discipline VARCHAR(50) DEFAULT NULL,
        function TEXT,
        event TEXT,
        discipline_id INTEGER DEFAULT NULL,
        coach_id INTEGER PRIMARY KEY AUTOINCREMENT,
        FOREIGN KEY (country_code) REFERENCES countries (country_code),
        FOREIGN KEY (discipline_id) REFERENCES disciplines (discipline_id)
    );
    ''')
    print("coaches table created successfully")

    conn.close()
