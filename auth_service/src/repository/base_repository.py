import uuid
from typing import Type, Union

from sqlmodel import Session, select, func
from pydantic import BaseModel

from src.core import config as app_config

PK_TYPE = Union[int, uuid.UUID]


class BaseRepository:
    def __init__(self, db_session: Session, model: Type[BaseModel]):
        self.db_session = db_session
        self.model = model
    
    def count(self, filters: list = None):
        filter = filters or []
        statement = select(func.count("*")).select_from(self.model).where(*filter)
        return self.db_session.exec(statement).one()
    
    def list(self, eager: bool = False, filters: list = None, **kwargs):
        ordering: str = kwargs.get("ordering", app_config.config.config.ORDERING)
        order_query = (
            getattr(self.model, ordering[1:]).desc()
            if ordering.startswith("-")
            else getattr(self.model, ordering).asc()
        )
        page = kwargs.get("page", None)
        page_size = kwargs.get("page_size", None)
        filters = filters or []
        statement = select(self.model).where(*filters).order_by(order_query)
        if page and page_size:
            statement = statement.offset((page - 1) * page_size).limit(page_size)
        results = self.db_session.exec(statement).all()
        return results

    def get(self, id: PK_TYPE, eager: bool = False):
        statement = select(self.model).where(self.model.id == id)
        result = self.db_session.exec(statement)
        return result.one()
    
    def create(self, model_instance: BaseModel):
        self.db_session.add(model_instance)
        self.db_session.commit()
        self.db_session.refresh(model_instance)
        return model_instance
    
    def update(self, model_instance: BaseModel):
        self.db_session.add(model_instance)
        self.db_session.commit()
        self.db_session.refresh(model_instance)
        return model_instance
    
    def delete(self, model_instance: BaseModel):
        self.db_session.delete(model_instance)
        self.db_session.commit()
        