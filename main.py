from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models import Document
from schemas import DocumentDetail, DocumentListItem

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/documents", response_model=list[DocumentListItem])
def list_documents(db: Session = Depends(get_db)):
    return db.scalars(select(Document).order_by(Document.id)).all()


@app.get("/api/documents/{document_id}", response_model=DocumentDetail)
def get_document(document_id: int, db: Session = Depends(get_db)):
    document = db.get(Document, document_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document