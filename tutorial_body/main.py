from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None
    tax: float | None = None

@app.get("/hello")
async def get_hello():
    return {
        "message": "Hello, World!"
    }

@app.post("/items")
async def create_item(item: Item):
    return item

@app.post("/items/price_with_tax")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict
