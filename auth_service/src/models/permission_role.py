import uuid
from sqlmodel import SQLModel, Field

class RolePermissionLink(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    role_id: uuid.UUID = Field(foreign_key="role.id")
    permission_id: int = Field(foreign_key="permission.id")
    
