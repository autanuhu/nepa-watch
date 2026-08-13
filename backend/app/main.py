from fastapi import FastAPI

app = FastAPI(
    title="NEPA Watch API",
    description="Open electricity outage intelligence platform for Africa.",
    version="0.1.0",
)


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
