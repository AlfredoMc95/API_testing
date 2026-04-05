from tests.utils.utils import assert_ok_response, assert_item_equal

def test_get_item(create_item, client):
    item = create_item("fruta", 40)
    res = client.get(f"/items/{item['id']}")

    assert_ok_response(res)
    assert_item_equal(res, item)
    print(item)