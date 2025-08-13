from typing import List, Optional
from sqlmodel import Session, select
from app.models.category import Category

def get_multi(session: Session) -> List[Category]:
    return session.exec(select(Category).order_by(Category.name)).all()

def get(session: Session, category_id: int) -> Optional[Category]:
    return session.get(Category, category_id)

def create(session: Session, *, obj_in: Category) -> Category:
    session.add(obj_in)
    session.commit()
    session.refresh(obj_in)
    return obj_in

def update(session: Session, *, db_obj: Category, obj_in: dict) -> Category:
    for k, v in obj_in.items():
        setattr(db_obj, k, v)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def remove(session: Session, *, db_obj: Category) -> None:
    session.delete(db_obj)
    session.commit()
