from fastapi import FastAPI
from typing import Optional
import uvicorn

app = FastAPI(debug=True)


@app.get("/")
async def read_root():
    return {"message": "Hello! Aman"}


@app.get("/home")
async def my_home():
    return {"message": "Welcome Home"}


@app.post("/branch")
async def read_root():
    return {"message": "i'm from CS branch"}

if __name__ == '__main__':
    uvicorn.run(app,host = "127.0.0.1",port = 8000)
