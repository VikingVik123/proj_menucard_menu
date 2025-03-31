from database.db import db
from sqlmodel import SQLModel, Field
from typing import Optional, List

class Menu(SQLModel, table=True):
    __tablename__ = "menu"
    