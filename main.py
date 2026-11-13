from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routes.users import user_router
from routes.events import event_router

# Добавил debug=True, чтобы видеть ошибки в браузере
app = FastAPI(title="Planner API — Игнатченко Владислав", debug=True)

# Подключаем роутеры (твой API)
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

# Настраиваем Jinja2 для HTML
templates = Jinja2Templates(directory="templates")

# Главная страница (UI)
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    # ИСПРАВЛЕННЫЙ СИНТАКСИС ДЛЯ НОВЫХ ВЕРСИЙ FASTAPI
    return templates.TemplateResponse(request=request, name="index.html")