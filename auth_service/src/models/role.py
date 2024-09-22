from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship

from src.models.mixins import DateHistoryMixin, UUIDPrimaryKeyMixin
from src.models.permission_role import RolePermissionLink

if TYPE_CHECKING:
    from src.models.user import User
    from src.models.permission import Permission


class Role(UUIDPrimaryKeyMixin, DateHistoryMixin, table=True):
    name: str = Field(nullable=False, unique=True)
    description: str | None = Field(nullable=True)
    users: list["User"] = Relationship(back_populates="role")
    permissions: list["Permission"] = Relationship(back_populates="roles", link_model=RolePermissionLink) 