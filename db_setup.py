# This script creates the structure of the database 

import sqlite3

def create_db():
    conn = sqlite3.connect("transactions.db")
    c = conn.cursor()

    # Create the table 'categories' if it does not exist
    c.execute('''CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT UNIQUE NOT NULL
    )''')

    # Create the table 'messages' if it does not exist
    c.execute('''CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        readable_date TEXT,
        address TEXT,
        body TEXT,
        amount INTEGER,
        balance INTEGER,
        contact_name TEXT,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories (id)
    )''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_db()
