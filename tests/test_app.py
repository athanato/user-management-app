import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_users_empty(client):
    """Ελέγχει ότι η λίστα χρηστών είναι αρχικά κενή."""
    response = client.get('/users')
    assert response.status_code == 200
    assert response.get_json() == []
