from database.db import initialize_database

# initialize_database()

# print("Database initialized successfully.")
from database.db import get_connection


connection = get_connection()

cursor = connection.cursor()

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table';
""")

tables = cursor.fetchall()

print("Tables in database:")

for table in tables:
    print(table[0])

connection.close()