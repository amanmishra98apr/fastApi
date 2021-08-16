import sqlalchemy
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
import uvicorn
from pydantic import BaseModel


app = FastAPI(debug=True)

print(sqlalchemy.__version__)

engine = create_engine('sqlite:///C:/Users/Acer/Desktop/aman.db', echo=True)

print("connection established")

meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String),
)
print("table created")

meta.create_all(engine)

# ins = students.insert().values(name="arvind", lastname="kumar")
# print(str(ins))
# result = conn.execute(ins)
s = students.select().where(students.c.id>2)
conn = engine.connect()
result = conn.execute(s)
row = result.fetchall()
print(row)


# print(result)
#
#
# row = result.fetchone()
# print(row)
# row = result.fetchone()
# print(row)
class Std(BaseModel):
    id: int
    name: str = None
    lastname: str = None


@app.get("/student/")
async def createItems():
    conn = engine.connect()
    result = conn.execute(s)
    row = result.fetchall()
    return row


@app.post("/student/")
async def postItems(std: Std):
    s = students.select().where(students.c.id == std.id)
    # s.where(students.c.id = std.id)
    conn = engine.connect()
    result = conn.execute(s)
    row = result.fetchall()
    return row


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
