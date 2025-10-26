# app.py
```python
from flask import Flask, request, jsonify
from integration_test.db import insert_user

flask_app = Flask(__name__)

@flask_app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username required"}), 400
    insert_user(username)
    return jsonify({"message": f"User {username} registered"}), 201
```

# db.py
```python
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
```

# test_integration.py

```python
import pytest

from integration_test.db import (init_db, get_users)
from integration_test.app import (flask_app)


@pytest.fixture(scope="module")
def client():
    init_db()
    with flask_app.test_client() as client:
        yield client

def test_register_user(client):
    response = client.post("/register", json={"username": "Alice"})
    assert response.status_code == 201
    assert "Alice" in get_users()
```