def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_documents(client):
    response = client.get("/api/documents")
    assert response.status_code == 200
    documents = response.json()
    assert len(documents) == 2
    assert documents[0] == {
        "id": 1,
        "title": "Introducere in inteligenta artificiala",
        "fileType": "pdf",
        "status": "pending",
    }


def test_get_document(client):
    response = client.get("/api/documents/2")
    assert response.status_code == 200
    document = response.json()
    assert document["id"] == 2
    assert document["title"] == "Notiuni de biologie"
    assert document["fileType"] == "txt"
    assert document["status"] == "pending"
    assert "uploadDate" in document


def test_document_not_found(client):
    response = client.get("/api/documents/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "Document not found"}


def test_document_id_must_be_a_number(client):
    response = client.get("/api/documents/abc")
    assert response.status_code == 422