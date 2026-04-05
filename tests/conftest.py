import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def item(client):
    return client.post("/items/", json={
        "name": "prado",
        "price": 50
    }).json()

@pytest.fixture
def create_item(client):
    def _create(name="test", price=10):
        res = client.post("/items/", json={
            "name": name,
            "price": price
        })
        return res.json()
    return _create