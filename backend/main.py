
from fastapi import FastAPI

from backend.database import engine, Base
from backend import models
from backend.auth import router as auth_router
from backend.products import router as products_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI E-commerce API")

app.include_router(auth_router)
app.include_router(products_router)


@app.get("/")
def home():
    return {"message": "E-commerce API is running"}