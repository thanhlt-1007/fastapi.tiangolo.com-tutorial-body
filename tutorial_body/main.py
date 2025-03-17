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
