from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Document
from app.schemas import DocumentDetail, DocumentListItem, DocumentCreate

router = APIRouter(prefix="/api/documents", tags=["documents"])


@router.get("", response_model=list[DocumentListItem])
def list_documents(db: Session = Depends(get_db)):
    return db.scalars(select(Document).order_by(Document.id)).all()


@router.get("/{document_id}", response_model=DocumentDetail)
def get_document(document_id: int, db: Session = Depends(get_db)):
    document = db.get(Document, document_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@router.post("", status_code=201)
def create_document(document_in: DocumentCreate, db: Session = Depends(get_db)):
    document = Document(title=document_in.title, file_type=document_in.file_type)
    db.add(document)
    db.commit()
    db.refresh(document)
    return {"message": "Document uploaded successfully", "id": document.id}


@router.delete("/{document_id}")
def delete_document(document_id: int, db: Session = Depends(get_db)):
    document = db.get(Document, document_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    db.delete(document)
    db.commit()
    return {"message": "Document deleted successfully"}