from fastapi import FastAPI
from app.routes import items
from app.core.database import Base, engine

def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()
app = FastAPI()
app.include_router(items.router)
