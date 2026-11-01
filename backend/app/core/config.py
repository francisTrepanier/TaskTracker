from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://taskuser:change_this_password@localhost:5432/tasks"
    JWT_SECRET: str = "change_me"

settings = Settings()