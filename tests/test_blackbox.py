# tests/test_blackbox.py
import pytest
from src.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_dashboard_access_while_logged_out(client):
    response = client.get('/dashboard')
    assert response.status_code == 302  # Expecting redirect to login

def test_dashboard_access_while_logged_in(client):
    with client.session_transaction() as sess:
        sess['loggedin'] = True
        sess['username'] = 'testuser'
    response = client.get('/dashboard')
    assert response.status_code == 200  # Expecting access to the dashboard
