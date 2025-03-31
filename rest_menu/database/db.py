import os
from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)

class database:
    def __init__(self):
        self.engine = engine

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)

db = database()
