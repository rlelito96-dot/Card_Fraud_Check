from fastapi import FastAPI

from app.api.v1 import fraud

app = FastAPI(title="Fraud Check Service", version="1.0")

app.include_router(fraud.router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Fraud Check Service is running!"}
