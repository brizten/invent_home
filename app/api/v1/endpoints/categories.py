from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from sqlmodel import Session
from app.api.deps import get_db
from app.schemas.category import CategoryCreate, CategoryUpdate
from app.models.category import Category
from app.crud import category as crud_category
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()

@router.get("")
def categories_page(request: Request, db: Session = Depends(get_db)):
    categories = crud_category.get_multi(db)
    return templates.TemplateResponse("categories.html", {"request": request, "title": "Категории", "now": request.state.now, "categories": categories})

@router.get("/new")
def new_category_form(request: Request):
    return templates.TemplateResponse("category_form.html", {"request": request, "title": "Новая категория", "now": request.state.now, "category": None})

@router.post("/new")
def create_category(name: str = Form(...), description: str | None = Form(None), db: Session = Depends(get_db)):
    obj = Category(name=name.strip(), description=(description or "").strip() or None)
    crud_category.create(db, obj_in=obj)
    return RedirectResponse(url="/categories", status_code=303)

@router.get("/{category_id}/edit")
def edit_category_form(category_id: int, request: Request, db: Session = Depends(get_db)):
    c = crud_category.get(db, category_id)
    if not c:
        raise HTTPException(404, "Категория не найдена")
    return templates.TemplateResponse("category_form.html", {"request": request, "title": "Редактирование категории", "now": request.state.now, "category": c})

@router.post("/{category_id}/edit")
def update_category(category_id: int, name: str = Form(...), description: str | None = Form(None), db: Session = Depends(get_db)):
    c = crud_category.get(db, category_id)
    if not c:
        raise HTTPException(404, "Категория не найдена")
    crud_category.update(db, db_obj=c, obj_in={"name": name.strip(), "description": (description or "").strip() or None})
    return RedirectResponse(url="/categories", status_code=303)

@router.post("/{category_id}/delete")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    c = crud_category.get(db, category_id)
    if c:
        # Обнулим category_id у связанных вещей — делается каскадом в UI-части items
        crud_category.remove(db, db_obj=c)
    return RedirectResponse(url="/categories", status_code=303)
