from fastapi import APIRouter, HTTPException
from models.menu import Menu
from database.db import db
from typing import List


router = APIRouter()

@router.get("/menu", response_model=List[Menu])
def get_menu():
    """
    Get all menu items.
    """
    session = db.get_session()
    try:
        menu_items = session.query(Menu).all()
        return menu_items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()
    
@router.post("/add_items", response_model=Menu)
def add_menu_item(item: Menu):
    """
    Add a new menu item.
    """
    session = db.get_session()
    try:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()