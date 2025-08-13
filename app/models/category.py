from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None

    items: List["Item"] = Relationship(back_populates="category")
