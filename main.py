from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

documents = [
    {
        "id": "D1",
        "title": "Introducere in inteligenta artificiala",
        "fileType": "pdf",
        "status": "pending",
    },
    {
        "id": "D2",
        "title": "Notiuni de biologie",
        "fileType": "txt",
        "status": "pending",
    },
]

@app.get("/api/documents")
def list_documents():
    return documents

@app.get("/api/documents/{document_id}")
def get_document(document_id: str):
    for document in documents:
        if document["id"] == document_id:
            return document

    raise HTTPException(status_code=404, detail="Document not found")
