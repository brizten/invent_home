from datetime import date
from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from sqlmodel import Session
from app.api.deps import get_db
from app.schemas.item import ItemCreate, ItemUpdate
from app.models.item import Item
from app.models.category import Category
from app.crud import item as crud_item
from app.crud import category as crud_category
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()

@router.get("")
def items_page(request: Request, q: str | None = None, category_id: int | None = None, sort: str = "new", db: Session = Depends(get_db)):
    categories = crud_category.get_multi(db)
    rows = crud_item.get_multi(db, q=q, category_id=category_id, sort=sort)
    return templates.TemplateResponse("index.html", {"request": request, "title": "Вещи", "now": request.state.now, "categories": categories, "items": rows, "q": q, "category_id": category_id, "sort": sort})

@router.get("/new")
def new_item_form(request: Request, db: Session = Depends(get_db)):
    categories = crud_category.get_multi(db)
    return templates.TemplateResponse("item_form.html", {"request": request, "title": "Новая вещь", "now": request.state.now, "item": None, "categories": categories})

@router.post("/new")
def create_item(
    name: str = Form(...),
    category_id: int | None = Form(None),
    location: str | None = Form(None),
    quantity: int = Form(1),
    unit: str | None = Form("шт"),
    value: float | None = Form(None),
    purchase_date: str | None = Form(None),
    notes: str | None = Form(None),
    photo_url: str | None = Form(None),
    db: Session = Depends(get_db),
):
    obj = Item(
        name=name.strip(),
        category_id=int(category_id) if category_id else None,
        location=(location or "").strip() or None,
        quantity=int(quantity or 0),
        unit=(unit or "").strip() or None,
        value=float(value) if value not in (None, "") else None,
        purchase_date=date.fromisoformat(purchase_date) if purchase_date else None,
        notes=(notes or "").strip() or None,
        photo_url=(photo_url or "").strip() or None,
    )
    crud_item.create(db, obj_in=obj)
    return RedirectResponse(url="/", status_code=303)

@router.get("/{item_id}/edit")
def edit_item_form(item_id: int, request: Request, db: Session = Depends(get_db)):
    item = crud_item.get(db, item_id)
    if not item:
        raise HTTPException(404, "Вещь не найдена")
    categories = crud_category.get_multi(db)
    return templates.TemplateResponse("item_form.html", {"request": request, "title": "Редактирование вещи", "now": request.state.now, "item": item, "categories": categories})

@router.post("/{item_id}/edit")
def update_item(
    item_id: int,
    name: str = Form(...),
    category_id: int | None = Form(None),
    location: str | None = Form(None),
    quantity: int = Form(1),
    unit: str | None = Form("шт"),
    value: float | None = Form(None),
    purchase_date: str | None = Form(None),
    notes: str | None = Form(None),
    photo_url: str | None = Form(None),
    db: Session = Depends(get_db),
):
    item = crud_item.get(db, item_id)
    if not item:
        raise HTTPException(404, "Вещь не найдена")
    updates = {
        "name": name.strip(),
        "category_id": int(category_id) if category_id else None,
        "location": (location or "").strip() or None,
        "quantity": int(quantity or 0),
        "unit": (unit or "").strip() or None,
        "value": float(value) if value not in (None, "") else None,
        "purchase_date": date.fromisoformat(purchase_date) if purchase_date else None,
        "notes": (notes or "").strip() or None,
        "photo_url": (photo_url or "").strip() or None,
    }
    crud_item.update(db, db_obj=item, obj_in=updates)
    return RedirectResponse(url="/", status_code=303)

@router.post("/{item_id}/delete")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = crud_item.get(db, item_id)
    if item:
        crud_item.remove(db, db_obj=item)
    return RedirectResponse(url="/", status_code=303)
