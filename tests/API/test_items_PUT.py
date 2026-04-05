from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_put_item():
    res = client.post("/items/",json={
        "name":"prado",
        "price": 55
    })

    item_id = res.json()["id"]

    response = client.put(f"/items/{item_id}",json={
        "price":80
    })

    assert response.status_code == 200
    assert response.json()["price"] == 80
