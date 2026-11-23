from datetime import datetime

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class DocumentListItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    file_type: str = Field(serialization_alias="fileType")
    status: str


class DocumentDetail(DocumentListItem):
    upload_date: datetime = Field(serialization_alias="uploadDate")

class DocumentCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    file_type: Literal["pdf", "docx", "txt"] = Field(validation_alias="fileType")