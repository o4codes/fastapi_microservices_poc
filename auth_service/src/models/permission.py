from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship

from src.models.mixins import DateHistoryMixin
from src.models.permission_role import RolePermissionLink

if TYPE_CHECKING:
    from src.models.role import Role

class Permission(DateHistoryMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    module: str = Field(nullable=False, unique=True)
    name: str = Field(nullable=False, unique=True)
    description: str | None = Field(nullable=True)
    roles: list["Role"] = Relationship(back_populates="permissions", link_model=RolePermissionLink)

