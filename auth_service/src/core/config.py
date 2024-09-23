from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)
    
    # general
    DEBUG: bool = Field(default=False)
    PROJECT_NAME: str = Field(default="Auth Service")
    PROJECT_NAME_CODE: str = Field(default="auth")
    PROJECT_VERSION: str = Field(default="v1")
    
    # database
    DB_NAME: str 
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_ENGINE: str
    
    # default pagination params
    PAGE: int = 1
    PAGE_SIZE: int = 20
    ORDERING: str = "-created_datetime"
    
    @computed_field
    def URL_PREFIX(self):
        return f"/api/{self.PROJECT_VERSION}"
    
    @computed_field
    def DB_URL(self):
        DATABASE_URI_FORMAT: str = "{db_engine}://{user}:{password}@{host}:{port}/{database}"
        DATABASE_URI = DATABASE_URI_FORMAT.format(
            db_engine=self.DB_ENGINE,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            database=self.DB_NAME,
        )
        return DATABASE_URI

config = AppConfig()
