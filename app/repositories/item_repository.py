from sqlalchemy.orm import Session
from app.models.item_model import Item

class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, price: float):
        item = Item(name=name, price=price)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def get_all(self):
        return self.db.query(Item).all()

    def get_by_id(self, item_id: int):
        return self.db.query(Item).filter(Item.id == item_id).first()

    def update(self, item_id: int, name: str, price: float):
        item = self.get_by_id(item_id)
        if not item:
            return None
        
        if name is not None:
            item.name = name

        if price is not None:
            item.price = price
        
        self.db.commit()
        self.db.refresh(item)
        return item

    def delete(self, item_id: int):
        item = self.get_by_id(item_id)
        if not item:
            return None
        self.db.delete(item)
        self.db.commit()
        return item