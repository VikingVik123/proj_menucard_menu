from fastapi import FastAPI
from typing import List
from routers.menu import router as menu
from models.menu import Menu
from database.db import db
import os
import uvicorn

app = FastAPI()
# Include the menu router
app.include_router(menu, prefix="/menu", tags=["menu"])

@app.get("/")
async def root():
    return {"message": "Welcome to the REST API for the menu!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=os.getenv("PORT") or 8000)