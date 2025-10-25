import sqlite3

DB_NAME = "test.db"

def init_db():
    db_connection = sqlite3.connect(DB_NAME)
    db_connection_cursor = db_connection.cursor()
    db_connection_cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)")
    db_connection.commit()
    db_connection.close()

def insert_user(username):
    db_connection = sqlite3.connect(DB_NAME)
    db_connection_cursor = db_connection.cursor()
    db_connection_cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
    db_connection.commit()
    db_connection.close()

def get_users():
    db_connection = sqlite3.connect(DB_NAME)
    db_connection_cursor = db_connection.cursor()
    db_connection_cursor.execute("SELECT username FROM users")
    users = [row[0] for row in db_connection_cursor.fetchall()]
    db_connection.close()
    return users
