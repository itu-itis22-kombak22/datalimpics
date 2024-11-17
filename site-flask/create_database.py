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

    conn.close()
