from fastapi import FastAPI
from typing import Optional
import uvicorn

app = FastAPI()

@app.get("/items")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

if __name__ == '__main__':
    uvicorn.run(app,host = "127.0.0.1",port = 8000)


