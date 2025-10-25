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