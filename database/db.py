import sqlite3
from pathlib import Path

DATABASE_PATH = Path("data/hospital.db")

def get_connection():

        DATABASE_PATH.parent.mkdir(exist_ok=True)
        return sqlite3.connect(DATABASE_PATH)

def initialize_database():
    conn = get_connection()

    with open("database/schema.sql", "r") as f:
          schema = f.read()

    conn.executescript(schema)
    conn.commit()
    conn.close()
    
