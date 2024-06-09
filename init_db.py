import sqlite3

def initialize_database():
    try:
        connection = sqlite3.connect('database.db')
        with open('schema.sql') as f:
            connection.executescript(f.read())

        with connection:
            cursor = connection.cursor()
            cursor.executemany("INSERT INTO posts (title, content) VALUES (?, ?)",
                               [('First Post', 'Content for the first post'),
                                ('Second Post', 'Content for the second post')])
    except sqlite3.Error as e:
        print("SQLite error:", e)
    finally:
        if connection:
            connection.close()

if __name__ == '__main__':
    initialize_database()



