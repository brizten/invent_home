from typing import Optional
from datetime import date
from sqlmodel import SQLModel

class ItemBase(SQLModel):
    name: str
    category_id: Optional[int] = None
    location: Optional[str] = None
    quantity: int = 1
    unit: Optional[str] = "шт"
    value: Optional[float] = None
    purchase_date: Optional[date] = None
    notes: Optional[str] = None
    photo_url: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemRead(ItemBase):
    id: int

class ItemUpdate(SQLModel):
    name: Optional[str] = None
    category_id: Optional[int] = None
    location: Optional[str] = None
    quantity: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    purchase_date: Optional[date] = None
    notes: Optional[str] = None
    photo_url: Optional[str] = None
