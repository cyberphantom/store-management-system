from pydantic import BaseModel

class Item(BaseModel):
    name: str
    quantity: int
    # Add other fields as necessary

