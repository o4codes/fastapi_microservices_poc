import uuid
from datetime import datetime

from sqlmodel import SQLModel, Field, Column, DateTime, func

class UUIDPrimaryKeyMixin(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

class DateHistoryMixin(SQLModel):
    created_datetime: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))
    last_modified_datetime: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now()))
    