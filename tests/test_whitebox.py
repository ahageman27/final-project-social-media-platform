import pytest
from flask import template_rendered
from contextlib import contextmanager
from src.main import app

@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_dashboard_logged_in(client):
    with client.session_transaction() as sess:
        sess['loggedin'] = True
        sess['username'] = 'testuser'
    with captured_templates(app) as templates:
        response = client.get('/dashboard')
        assert response.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template[0].name == 'dashboard.html'
        assert 'username' in context and context['username'] == 'testuser'

def test_dashboard_not_logged_in(client):
    response = client.get('/dashboard')
    assert response.status_code == 302
    assert '/login' in response.headers['Location']
