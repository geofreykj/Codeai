from pydantic_settings import BaseSettings, SettingsConfigDict

"""
Application configuration.

Loads environment variables and exposes them through a typed Settings object.
"""
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
        )
    app_name: str
    app_version: str
    app_description: str
    debug: bool
    host: str
    port: int
    database_url: str
    secret_key: str

settings = Settings()