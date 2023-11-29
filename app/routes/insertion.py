from fastapi import APIRouter
from ..models import Item
import json

router = APIRouter()

@router.post("/insertion")
async def insert_item(item: Item):
    # Implement logic to insert item
    # Update the items.json file accordingly
    return {"message": "Item inserted successfully"}

