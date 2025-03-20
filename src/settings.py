import sys
from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    database_username: str
    database_password: str
    database_host: str
    database_port: int
    database_name: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

try:
    settings = Settings()
except Exception as e:
    print(f"Error: {e}")
    print("Please, check your environment variables and .env file.")
    sys.exit(1)
