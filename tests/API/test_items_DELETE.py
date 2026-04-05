from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_item():
    res = client.post("/items/",json={
        "name":"prado",
        "price": 55
    })

    item_id = res.json()["id"]
    response = client.delete(f"/items/{item_id}")

    assert response.status_code == 200
