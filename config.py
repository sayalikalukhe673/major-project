import os
from functools import lru_cache
from typing import Literal

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()

class settings (BaseSettings):
    App_Name: str = os.getenv("APP_NAME" , "FastApi Application")
    ENV: Literal["developments", "stagging", "production"] = os.getenv("ENV", "developments")
    DEBUG: bool = os.getenv("DEBUG","true").lower() in ("true","1","yes")
    VERSION: str = os.getenv("VERSION","1.0.0")

    HOST: str= os.getenv("HOST","0.0.0.0")
    PORT: int = int(os.getenv("PORT","8000"))
    RELOAD: bool = os.getenv("RELOAD","true").lower() in ("true","1","yes")


    ALLOWED_ORIGINS: list[str] = os.getenv(
        "ALLOWED_ORIGINS",
        "*",
        ).split(",")
    

    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY",",")

    LOG_LEVEL: str = os.getenv("LOG_LEVEL","INFO")

    class confif:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> settings:

    return settings()


settings = get_settings()


