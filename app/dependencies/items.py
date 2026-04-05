from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.item_repository import ItemRepository
from app.services.item_service import ItemService

def get_item_service(db: Session = Depends(get_db)):
    repo = ItemRepository(db)
    return ItemService(repo)