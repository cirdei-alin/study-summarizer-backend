from fastapi import FastAPI

from app.routers import documents

app = FastAPI(title="The Study Summarizer API")

app.include_router(documents.router)


@app.get("/health")
def health():
    return {"status": "ok"}