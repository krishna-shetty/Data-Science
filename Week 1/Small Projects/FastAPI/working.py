from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

@app.get("/")
def home():
    return {"Data": "Testing"}

@app.get('/about')
def about():
    return {"Data": "About"}

inventory = {}

@app.get("/get-by-item/{item_id}")
def get_item(item_id: int = Path(..., description="The ID of the item to be viewed")):
    if item_id in inventory:
        return inventory[item_id]
    return HTTPException(status_code = 404, detail = "The passed ID was not found")

@app.get("/get-by-name/")
def get_item(name: str = Query(None, description = "The name of the item to be returned")):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code = 404, detail = "The passed name was not found")

@app.post("/create-item/{item_id}")
def create_item(item: Item, item_id:int = Path(..., description="The ID of the item to be created")):
    if item_id in inventory:
        raise HTTPException(status_code = 403, detail = "The passed ID already exists")

    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item: UpdateItem, item_id: int = Path(..., description="The ID of the item to be updated")):
    if item_id not in inventory:
        raise HTTPException(status_code = 404, detail = "The passed ID was not found")

    if item.name != None:
        inventory[item_id].name = item.name
    
    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand
    
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description = "The ID of the item to be deleted")):
    if item_id not in inventory:
        raise HTTPException(status_code = 404, detail = "The  ID was not found")

    del inventory[item_id]
    return {"Operation": "Successful"}