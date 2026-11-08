# Study Summarizer — Backend

Backend API for a web application that will help users generate
summaries from uploaded study documents.

Built with Python and FastAPI.

## Current functionality

The API currently provides:

- `GET /health` — checks that the API responds.
- `GET /api/documents` — returns the sample document list.
- `GET /api/documents/{document_id}` — returns a sample document by ID.
  Returns HTTP 404 if the document does not exist.

## Development status

Document data is currently stored in a hardcoded Python list for
development and learning purposes.

File upload, database persistence, and AI summarization are planned
for later stages.

## Requirements

- Python 3.15.2 — the version used during development
- Git

## Local setup — Windows with Git Bash

Clone the repository and enter its directory:

```bash
git clone https://github.com/cirdei-alin/study-summarizer-backend.git
cd study-summarizer-backend
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the application

From the repository directory, with the virtual environment active:

```bash
python -m uvicorn main:app --reload
```

The API runs locally at http://127.0.0.1:8000.

Interactive API documentation is available at:
http://127.0.0.1:8000/docs

To stop the server, press Ctrl+C in the terminal.

## Manual checks

With the server running, test the following requests using `/docs`:

| Request | Expected result |
| --- | --- |
| `GET /health` | HTTP 200 and `{"status":"ok"}` |
| `GET /api/documents` | HTTP 200 and the sample document list |
| `GET /api/documents/D1` | HTTP 200 and document D1 |
| `GET /api/documents/D99` | HTTP 404 and `{"detail":"Document not found"}` |