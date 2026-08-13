from fastapi import FastAPI

from app.routes.outages import router as outages_router


app = FastAPI(
    title="NEPA Watch API",
    description="Open electricity outage intelligence platform for Africa.",
    version="0.1.0",
)


app.include_router(outages_router)


@app.get("/")
def root():
    return {
        "name": "NEPA Watch",
        "version": "0.1.0",
        "status": "online",
        "message": "NEPA Watch API is running.",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
