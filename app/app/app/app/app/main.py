from fastapi import FastAPI
from .database import Base, engine

app = FastAPI(title="Strativ Task Management API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "Task Management API is running"
    }
