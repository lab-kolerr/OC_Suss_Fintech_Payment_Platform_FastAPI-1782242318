import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user():
    response = client.post('/api/users', json={'email': 'test@example.com', 'password': 'securepassword'})
    assert response.status_code == 200
    assert response.json() == {'email': 'test@example.com'}