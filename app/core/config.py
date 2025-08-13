from pydantic import BaseModel
from typing import Optional

class Settings(BaseModel):
    app_name: str = "Домашняя инвентаризация"
    debug: bool = True
    database_url: str = "sqlite:///inventory.db"

settings = Settings()
