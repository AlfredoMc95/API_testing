def assert_ok_response(res):
    assert res.status_code == 200

def assert_item_equal(res, item):
    data = res.json()
    assert data["name"] == item["name"]
    assert data["price"] == item["price"]
    assert "id" in data