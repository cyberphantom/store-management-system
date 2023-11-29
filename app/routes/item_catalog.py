from fastapi import APIRouter
from ..models import Item
import json

router = APIRouter()

@router.get("/items")
async def get_items():
    with open('data/items.json', 'r', encoding='utf-8') as file:
        items = json.load(file)
    return items

@router.post("/items/add")
async def add_item(item: Item):
    with open('data/items.json', 'r+', encoding='utf-8') as file:
        items = json.load(file)
        items.append(item.dict())
        file.seek(0)
        json.dump(items, file, ensure_ascii=False)
    return {"message": "Item added successfully"}

