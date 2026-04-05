from pydantic import BaseModel

# Lo que envía el usuario
class ItemCreate(BaseModel):
    name: str
    price: float

# Lo que responde la API
class Item(ItemCreate):
    id: int

class ItemUpdate(BaseModel):
    name: str | None = None
    price: float | None = None