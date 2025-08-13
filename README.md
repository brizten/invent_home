# Home Inventory (FastAPI + SQLModel)

## Quickstart

# Home Inventory

FastAPI-приложение для инвентаризации вещей в доме с использованием SQLModel и SQLite.

---

##  Быстрый старт

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
Открой в браузере: http://127.0.0.1:8000
GitHub

Структура проекта
csharp
Копировать
Редактировать
app/
├── api/
│   └── v1/
│       ├── endpoints/
│       │   ├── categories.py
│       │   └── items.py
│       └── router.py
├── core/
│   └── config.py
├── crud/
│   ├── category.py
│   └── item.py
├── db/
│   └── session.py
├── models/
│   ├── base.py
│   ├── category.py
│   └── item.py
├── schemas/
│   ├── category.py
│   └── item.py
├── templates/         # Jinja2-шаблоны
├── static/            # CSS / ассеты
└── main.py            # Точка входа FastAPI
inventory.db           # База SQLite (по умолчанию)
GitHub

Описание
Это простое и функциональное API на FastAPI, которое позволяет:

Добавлять, изменять и удалять категории и предметы.

Использовать шаблоны Jinja2 для веб-интерфейса.

Использовать SQLite (inventory.db) в качестве хранилища данных.

Особенности
Современный фреймворк FastAPI + SQLModel.

Чистая архитектура: разделение слоёв API, CRUD, моделей и схем.

Поддержка HTML-шаблонов для фронтенда (Jinja2) и статических файлов.

Лёгкая настройка и запуск.

Как использовать
Поднимите приложение (см. «Быстрый старт»).

Перейдите по адресу: http://127.0.0.1:8000.

Используйте API (Swagger UI доступен по /docs), либо веб-интерфейс (например, через HTML-шаблоны).

Добавляйте категории и предметы, взаимодействуйте через веб-формы или API.

Конфигурация
Настройки (например, путь до БД, параметры CORS и прочие) вынесены в app/core/config.py.

SQLite по умолчанию — файл inventory.db. При необходимости можно переключиться на другую БД, изменив настройки в config.py.

Зависимости
Проект использует Python и требует установки пакетов из requirements.txt:
GitHub

Идеи для улучшения
Подключить PostgreSQL или другую СУБД вместо SQLite.

Добавить аутентификацию/авторизацию пользователей.

Улучшить веб-интерфейс (дизайн, UX).

Написать тесты (unit, integration).

Добавить Docker-конфигурацию и CI/CD (GitHub Actions).

Ввести пагинацию, фильтрацию, сортировку предметов.

