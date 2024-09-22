import uuid
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from src.models.mixins import DateHistoryMixin, UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from src.models.role import Role


class User(DateHistoryMixin, UUIDPrimaryKeyMixin, table=True):
    """
    Holds Auth credentials information for users
    """
    email: str = Field(unique=True, index=True, nullable=False)
    password: str = Field(nullable=False)
    role_id: uuid.UUID | None = Field(default=None, foreign_key="role.id")
    role: "Role" | None  = Relationship(back_populates="users")