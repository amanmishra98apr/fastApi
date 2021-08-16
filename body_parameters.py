from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI(debug = True)


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/all_items/")
async def createItems(item: Item):
    return item

@app.post("/items/")
async def createItems(item: Item):
    item_dict = item.dict()
    total = item.price + item.tax
    item_dict.update({"total amount": total})
    return item_dict


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)

