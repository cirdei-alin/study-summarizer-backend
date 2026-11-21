from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class DocumentListItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    file_type: str = Field(serialization_alias="fileType")
    status: str


class DocumentDetail(DocumentListItem):
    upload_date: datetime = Field(serialization_alias="uploadDate")