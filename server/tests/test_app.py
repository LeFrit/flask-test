from flask.testing import FlaskClient
import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client: FlaskClient):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello World!' in response.data
