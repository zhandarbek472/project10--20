from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str
    debug: bool
    app_host: str
    app_port: int

    class Config:
        env_file = ".env"
        env_prefix = "APP_"
