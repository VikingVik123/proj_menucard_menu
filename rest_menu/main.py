from fastapi import FastAPI
from typing import List
from routes import menu
from models.menu import Menu  # Assuming this is the correct path for the Menu model
from database.db import db
import uvicorn

app = FastAPI()
db.create_db_and_tables()
# Include the menu router
app.include_router(menu.router, prefix="/menu", tags=["menu"])

@app.get("/")
async def root():
    return {"message": "Welcome to the REST API for the menu!"}


if __name__ == "__main__":  # This ensures that the app runs only when executed directly
    uvicorn.run(app, host="127.0.0.1", port=8000)