# This script inserts the data into the established database.

import sqlite3
from parse_sms import parse_sms_xml

def insert_messages(messages):
    conn = sqlite3.connect("transactions.db")
    c = conn.cursor()

    for msg in messages:
        # Get or insert category
        c.execute("INSERT OR IGNORE INTO categories (category) VALUES (?)", (msg['category'],))
        c.execute("SELECT id FROM categories WHERE category=?", (msg['category'],))
        category_id = c.fetchone()[0]

        # Avoid duplicates by checking unique body + date
        c.execute("SELECT * FROM messages WHERE body=? AND date=?", (msg['body'], msg['date']))
        if c.fetchone(): # gets the first matching row, if it exists.
            continue # If the row already exists, skip the current iteration.

        c.execute('''INSERT INTO messages 
            (date, readable_date, address, body, amount, balance, contact_name, category_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
            (msg['date'], msg['readable_date'], msg['address'], msg['body'],
             msg['amount'], msg['balance'], msg['contact_name'], category_id))

    conn.commit()
    conn.close()
