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

def test_create_document(client):
    response = client.post(
        "/api/documents",
        json={"title": "Retele de calculatoare", "fileType": "docx"},
    )
    assert response.status_code == 201
    assert response.json() == {"message": "Document uploaded successfully", "id": 3}

    new_document = client.get("/api/documents/3").json()
    assert new_document["title"] == "Retele de calculatoare"
    assert new_document["fileType"] == "docx"
    assert new_document["status"] == "pending"


def test_create_document_rejects_unknown_file_type(client):
    response = client.post("/api/documents", json={"title": "Poza", "fileType": "jpg"})
    assert response.status_code == 422


def test_create_document_requires_title(client):
    response = client.post("/api/documents", json={"title": "", "fileType": "pdf"})
    assert response.status_code == 422


def test_delete_document(client):
    response = client.delete("/api/documents/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Document deleted successfully"}

    assert client.get("/api/documents/1").status_code == 404
    assert len(client.get("/api/documents").json()) == 1


def test_delete_missing_document(client):
    response = client.delete("/api/documents/99")
    assert response.status_code == 404

def test_update_document_title(client):
    response = client.patch("/api/documents/1", json={"title": "Inteligenta artificiala - curs 1"})
    assert response.status_code == 200
    document = response.json()
    assert document["title"] == "Inteligenta artificiala - curs 1"
    assert document["fileType"] == "pdf"

    assert client.get("/api/documents/1").json()["title"] == "Inteligenta artificiala - curs 1"


def test_update_document_file_type(client):
    response = client.patch("/api/documents/2", json={"fileType": "docx"})
    assert response.status_code == 200
    document = response.json()
    assert document["fileType"] == "docx"
    assert document["title"] == "Notiuni de biologie"


def test_update_document_rejects_empty_title(client):
    response = client.patch("/api/documents/1", json={"title": ""})
    assert response.status_code == 422


def test_update_missing_document(client):
    response = client.patch("/api/documents/99", json={"title": "Nu exista"})
    assert response.status_code == 404