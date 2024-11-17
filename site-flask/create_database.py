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