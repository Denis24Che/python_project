import sqlite3
import os
import datetime

db_path = 'db/database.db'  # ensure the directory exists

# ensure directory exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Optional: create tables if they don't exist (adjust columns/types as needed)
with sqlite3.connect(db_path) as db:
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY,
            amount INTEGER,
            payment_date REAL,  -- store as timestamp
            expense_id INTEGER,
            FOREIGN KEY(expense_id) REFERENCES expenses(id)
        )
    """)
    db.commit()

# Insert some expenses (uncomment if you want to insert)
with sqlite3.connect(db_path) as db:
    cursor = db.cursor()
    queries = [
        """INSERT INTO expenses (id, name) VALUES(1, 'denis')""",
        """INSERT INTO expenses (id, name) VALUES(2, 'ivashka')""",
        """INSERT INTO expenses (id, name) VALUES(3, 'pam')"""
    ]
    # To avoid duplicates on rerun, you might want to guard with IF NOT EXISTS or handle exceptions
    for q in queries:
        cursor.execute(q)
    db.commit()

def get_timestamp(y, m, d):
    return datetime.datetime(y, m, d).timestamp()

# Prepare payments: list of tuples (id, amount, payment_date, expense_id)
insert_payments = [
    (1, 120, get_timestamp(2025, 10, 2), 1),
    (2, 120, get_timestamp(2025, 10, 2), 1),
    (3, 120, get_timestamp(2025, 10, 2), 1),
    (4, 120, get_timestamp(2025, 10, 2), 1),
    (5, 120, get_timestamp(2025, 10, 2), 1),
    (6, 120, get_timestamp(2025, 10, 2), 1),
]

with sqlite3.connect(db_path) as db:
    cursor = db.cursor()
    query = """INSERT INTO payments (id, amount, payment_date, expense_id) VALUES (?, ?, ?, ?)"""
    cursor.executemany(query, insert_payments)
    db.commit()
