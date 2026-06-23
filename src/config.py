import os
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    JWT_SECRET: str = Field(..., env="JWT_SECRET")
    PORT: int = Field(8000, env="PORT")

    class Config:
        env_file = ".env"

def get_settings() -> Settings:
    return Settings()