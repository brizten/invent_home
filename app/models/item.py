from datetime import datetime, date
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    location: Optional[str] = None
    quantity: int = 1
    unit: Optional[str] = "шт"
    value: Optional[float] = None
    purchase_date: Optional[date] = None
    notes: Optional[str] = None
    photo_url: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    category: Optional["Category"] = Relationship(back_populates="items")
