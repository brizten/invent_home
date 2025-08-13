# Home Inventory (FastAPI + SQLModel)

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000

## Project layout

```
app/
  api/
    v1/
      endpoints/
        categories.py
        items.py
      router.py
    deps.py
  core/
    config.py
  crud/
    category.py
    item.py
  db/
    session.py
  models/
    base.py
    category.py
    item.py
  schemas/
    category.py
    item.py
  templates/           # Jinja2 templates
  static/              # CSS / assets
  main.py              # FastAPI entrypoint
```

SQLite database is stored in `inventory.db` by default.
