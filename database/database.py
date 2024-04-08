import sqlite3

conn = sqlite3.connect('python_bible.db')

c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS person
            id INTEGER PRIMARY KEY
            first_name TEXT,
            last_name TEXT,
            age INTEGER""")

conn.commit()

c.execute("""INSERT INTO persons VALUES
 ('John', 'Smith', 25),
 ('Anna', 'Smith', 30),
 ('Mike', 'Johnson', 40)""")

conn.commit()
conn.close()