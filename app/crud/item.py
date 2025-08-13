from typing import List, Optional
from sqlmodel import Session, select
from app.models.item import Item
from app.models.category import Category

def get_multi(session: Session, *, q: Optional[str] = None, category_id: Optional[int] = None, sort: str = "new"):
    stmt = (
        select(
            Item.id,
            Item.name,
            Category.name.label("category_name"),
            Item.location,
            Item.quantity,
            Item.unit,
            Item.value,
            Item.purchase_date,
            Item.notes,
            Item.photo_url,
        )
        .select_from(Item)
        .join(Category, isouter=True)
    )
    if q:
        like = f"%{q}%"
        stmt = stmt.where((Item.name.ilike(like)) | (Item.location.ilike(like)) | (Item.notes.ilike(like)))
    if category_id:
        stmt = stmt.where(Item.category_id == category_id)

    if sort == "name":
        stmt = stmt.order_by(Item.name.asc())
    elif sort == "value":
        stmt = stmt.order_by(Item.value.desc().nulls_last())
    else:
        stmt = stmt.order_by(Item.created_at.desc())

    rows = session.exec(stmt).all()
    return rows

def get(session: Session, item_id: int) -> Optional[Item]:
    return session.get(Item, item_id)

def create(session: Session, *, obj_in: Item) -> Item:
    session.add(obj_in)
    session.commit()
    session.refresh(obj_in)
    return obj_in

def update(session: Session, *, db_obj: Item, obj_in: dict) -> Item:
    for k, v in obj_in.items():
        setattr(db_obj, k, v)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def remove(session: Session, *, db_obj: Item) -> None:
    session.delete(db_obj)
    session.commit()
