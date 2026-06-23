from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

items = []

@app.post('/items/', response_model=Item)
async def create_item(item: Item) -> Item:
    """
    Create a new item.
    
    Parameters:
    - item: Item object to be created.
    
    Returns:
    - The created Item object.
    """
    try:
        items.append(item)
        return item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/items/', response_model=List[Item])
async def read_items() -> List[Item]:
    """
    Retrieve all items.
    
    Returns:
    - A list of Item objects.
    """
    try:
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/items/{item_id}', response_model=Item)
async def read_item(item_id: int) -> Item:
    """
    Retrieve an item by its ID.
    
    Parameters:
    - item_id: ID of the item to retrieve.
    
    Returns:
    - The Item object with the specified ID.
    """
    try:
        for item in items:
            if item.id == item_id:
                return item
        raise HTTPException(status_code=404, detail='Item not found')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete('/items/{item_id}', response_model=Item)
async def delete_item(item_id: int) -> Item:
    """
    Delete an item by its ID.
    
    Parameters:
    - item_id: ID of the item to delete.
    
    Returns:
    - The deleted Item object.
    """
    try:
        for index, item in enumerate(items):
            if item.id == item_id:
                return items.pop(index)
        raise HTTPException(status_code=404, detail='Item not found')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))