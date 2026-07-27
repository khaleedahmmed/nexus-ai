
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal

class AppSettings(BaseSettings):
    app_name: str = "Nexus AI"
    app_env: Literal["development", "staging", "production"] = (
        "development"
    )
    debug: bool = True

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8" , extra="ignore"
    )
    
