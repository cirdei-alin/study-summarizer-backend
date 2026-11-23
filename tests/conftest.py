import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app
from app.models import Document

test_engine = create_engine(os.getenv("TEST_DATABASE_URL"))
TestSessionLocal = sessionmaker(bind=test_engine)


@pytest.fixture
def client():
    Base.metadata.create_all(bind=test_engine)

    db = TestSessionLocal()
    db.add_all(
        [
            Document(title="Introducere in inteligenta artificiala", file_type="pdf"),
            Document(title="Notiuni de biologie", file_type="txt"),
        ]
    )
    db.commit()

    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)

    app.dependency_overrides.clear()
    db.close()
    Base.metadata.drop_all(bind=test_engine)