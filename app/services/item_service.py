from app.repositories.item_repository import ItemRepository

class ItemService:
    def __init__(self, repo: ItemRepository):
        self.repo = repo

    def get_items(self):
        return self.repo.get_all()

    def create_item(self, item):
        return self.repo.create(item.name, item.price)

    def get_item(self, item_id: int):
        return self.repo.get_by_id(item_id)

    def update_item(self, item_id: int, item):
        return self.repo.update(item_id, item.name, item.price)

    def delete_item(self, item_id: int):
        return self.repo.delete(item_id)