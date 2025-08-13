from datetime import datetime
from pathlib import Path
from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import SQLModel, Session
from app.db.session import engine
from app.api.deps import get_db
from app.crud import item as crud_item, category as crud_category
from app.api.v1.endpoints import items as items_endpoints
from app.api.v1.endpoints import categories as categories_endpoints

app = FastAPI(title="Домашняя инвентаризация", debug=True)

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.middleware("http")
async def add_now_to_request(request: Request, call_next):
    request.state.now = datetime.now()
    return await call_next(request)

# Главная СТРАНИЦА с нормальным Depends — тут НЕ звоним items_page(...)
@app.get("/")
def home(request: Request,
         q: str | None = None,
         category_id: int | None = None,
         sort: str = "new",
         db: Session = Depends(get_db)):
    categories = crud_category.get_multi(db)
    rows = crud_item.get_multi(db, q=q, category_id=category_id, sort=sort)
    return templates.TemplateResponse("index.html", {
        "request": request, "title": "Вещи", "now": request.state.now,
        "categories": categories, "items": rows,
        "q": q, "category_id": category_id, "sort": sort
    })

# Подключаем роутеры — с префиксами!
app.include_router(items_endpoints.router, prefix="/items")
app.include_router(categories_endpoints.router, prefix="/categories")


# Healthcheck
@app.get("/healthz")
def healthz():
    return {"ok": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=False, log_level="debug")

