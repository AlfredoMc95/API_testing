from fastapi import APIRouter, Depends, HTTPException
from app.schemas.item import ItemCreate, Item, ItemUpdate
from app.dependencies.items import get_item_service

router = APIRouter(prefix="/items")

@router.get("/", response_model=list[Item])
def get_items(service=Depends(get_item_service)):
    return service.get_items()

@router.post("/", response_model=Item)
def create_item(item: ItemCreate, service=Depends(get_item_service)):
    return service.create_item(item)

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int, service=Depends(get_item_service)):
    get = service.get_item(item_id)
    if not get:
        raise HTTPException(status_code=404, detail="Item not found")
    return get

@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate, service=Depends(get_item_service)):
    updated = service.update_item(item_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated

@router.delete("/{item_id}", response_model=Item)
def delete_item(item_id: int, service=Depends(get_item_service)):
    deleted = service.delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return deleted