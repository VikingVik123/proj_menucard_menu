from database.db import db
from sqlmodel import SQLModel, Field
from typing import Optional, List

class Menu(SQLModel, table=True):
    __tablename__ = "menu"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(description="Name of the item on the menu")
    description: str = Field(description="Description of the item")
    price: float = Field(description="Price of the item")
    img_url: str = Field(description="Image URL of the item")
    