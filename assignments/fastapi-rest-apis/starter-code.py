from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Item API")

items = [
    {"id": 1, "name": "Laptop", "price": 999.99, "in_stock": True},
    {"id": 2, "name": "Mouse", "price": 29.99, "in_stock": True},
]


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


@app.get("/")
def read_root():
    return {"message": "Welcome to the Item API"}


# TODO: Add GET, POST, PUT, and DELETE routes for items
