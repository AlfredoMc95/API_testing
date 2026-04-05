from pydantic_settings import BaseSettings, SettingsConfigDict

class settings(BaseSettings):
    app_name: str
    debug: bool
    database_url: str

    model_config = SettingsConfigDict(env_file=".env")

    
settings = settings()