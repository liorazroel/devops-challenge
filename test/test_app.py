from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_default_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.text == "Welcome to my secret code service!"

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'container' in data
    assert 'project' in data

def test_extract_secret_code(client):
    response = client.get('/secret')
    assert response.status_code == 200
    data = response.get_json()
    assert 'secret_code' in data