from app.app import app

def test_users_endpoint():
    client = app.test_client()
    response = client.get('/users')
    assert response.status_code == 200
