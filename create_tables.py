from app.database import Base, engine
from app import models  # noqa: F401  (îl importăm ca Base să afle de tabelul Document)

Base.metadata.create_all(bind=engine)
print("Tabelele au fost create.")