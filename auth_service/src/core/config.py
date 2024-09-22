from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)
    
    debug: bool = Field(default=False)
    db_url: str

config = AppConfig()
