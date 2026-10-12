from fastapi import FastAPI
from app.database import engine, BASE
from app import models
from app.routers import user

BASE.metadata.create_all(bind=engine)

app = FastAPI(title="HRM CRUD")

app.include_router(user.router)

@app.get("/")
def home():
    return {"message": "Welcome to the HRM CRUD API"}
