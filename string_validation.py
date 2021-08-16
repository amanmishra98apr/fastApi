from fastapi import FastAPI, Query
from typing import List
# from typing import Optional
import uvicorn

app = FastAPI(debug = True)


@app.get("/items/")
async def show_items(item_id: str = Query(None, max_length=10, min_length=5)):
    results = {"items": [{"item_id": "pen"}, {"item_id": "pencil"}]}
    if item_id:
        results.update({"item_id": item_id})
    return results


@app.get("/myitems/")
async def show_items(item_id: str = Query(..., max_length=10, min_length=5)):
    results = {"items": [{"item_id": "pen"}, {"item_id": "pencil"}]}
    if item_id:
        results.update({"item_id": item_id})
    return results

@app.get("/listitems/")
async def show_items(item_id: List[str] = Query(None, max_length=10, min_length=5)):
    results = {"items": [{"item_id": "pen"}, {"item_id": "pencil"}]}
    if item_id:
        results.update({"item_id": item_id})
    return results



if __name__ == '__main__':
    uvicorn.run(app, host = "127.0.0.1", port = 8000)

# we can pass any other default parameter inside Query