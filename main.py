from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello! World"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/id/{id}")
def idFun(id: int):
    return {"item_id": id}

@app.get("/name/{name}")
def idFun(name: str):
    return {"name": name}

