from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_document_not_found():
    response = client.get("/api/documents/D99")
    assert response.status_code == 404
    assert response.json() == {"detail": "Document not found"}

def test_get_document():
    response = client.get("/api/documents/D2")
    assert response.status_code == 200
    assert response.json() == {
       "id": "D2",
        "title": "Notiuni de biologie",
        "fileType": "txt",
        "status": "pending",
    }

def test_list_documents():
    response = client.get("/api/documents")
    assert response.status_code == 200
    documents = response.json()
    assert isinstance(documents, list)
    assert len(documents) == 2
    assert [document["id"] for document in documents] == ["D1", "D2"]