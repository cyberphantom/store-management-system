from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import json

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Model for items
class Item(BaseModel):
    name: str
    quantity: int
    description: str = None
    price: float = None

# Read and write data to the JSON file
def read_items():
    with open('data/items.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def write_items(items):
    with open('data/items.json', 'w', encoding='utf-8') as file:
        json.dump(items, file, ensure_ascii=False)

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/item-catalog", response_class=HTMLResponse)
async def item_catalog(request: Request):
    items = read_items()
    return templates.TemplateResponse("item_catalog.html", {"request": request, "items": items})

@app.post("/items/add")
async def add_item(item: Item):
    items = read_items()
    items.append(item.dict())
    write_items(items)
    return {"message": "Item added successfully"}

@app.get("/purchase", response_class=HTMLResponse)
async def purchase_page(request: Request):
    return templates.TemplateResponse("purchase.html", {"request": request})

@app.post("/purchase")
async def make_purchase(name: str = Form(...), quantity: int = Form(...)):
    items = read_items()
    for item in items:
        if item['name'] == name and item['quantity'] >= quantity:
            item['quantity'] -= quantity
            write_items(items)
            return {"message": "Purchase successful"}
    return {"error": "Item not available or insufficient quantity"}

@app.get("/insertion", response_class=HTMLResponse)
async def insertion_page(request: Request):
    return templates.TemplateResponse("insertion.html", {"request": request})

@app.post("/insertion")
async def insert_item(item: Item):
    items = read_items()
    items.append(item.dict())
    write_items(items)
    return {"message": "Item inserted successfully"}

# More routes can be added as per your application's requirements
