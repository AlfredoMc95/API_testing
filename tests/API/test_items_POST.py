from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_post_item():
    response  = client.post("/items/",json={
        "name":"fruta",
        "price": 40
    })

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "fruta"
    assert data["price"] == 40
    assert "id" in data