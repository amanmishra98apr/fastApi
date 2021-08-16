from fastapi import FastAPI
from typing import Optional
import uvicorn
from enum import Enum


class ModelName(str,Enum):
    name = "aman"
    branch = 'cs'
    roll_no = '21'


app = FastAPI(debug=True)


@app.get("/roll/{model_name}")
async def rollNo(model_name: ModelName):
    return {"Roll Number": model_name.roll_no}


@app.get("/id/{id}")
async def emp_id(id: int):
    return {"Employee ID": id}


@app.get("/files/{file_path: path")
async def file_pathFun(file_path: str):
    return {"file_path": file_path}

if __name__ == '__main__':
    uvicorn.run(app,host = "127.0.0.1",port = 8000)

