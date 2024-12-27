# # FastAPI + Uvicorn + Docker Compose

Этот проект представляет собой базовое приложение **FastAPI**, которое работает с базой данных **SQLite** и предоставляет API для управления терминологией через CRUD-операции. Проект использует **Docker** и **Docker Compose**.

## Структура проекта


        glossary-api/
        ├── app/
        │   ├── __init__.py
        │   ├── main.py
        │   ├── models.py
        │   ├── schemas.py
        │   └── database.py
        ├── Dockerfile
        ├── docker-compose.yml
        ├── requirements.txt
        ├── README.md
        └── .gitignore


Этот проект реализует API для работы с глоссарием терминов. Он поддерживает следующие операции:
- Получение списка всех терминов.
- Получение информации о конкретном термине по ключевому слову.
- Добавление нового термина с описанием.
- Обновление существующего термина.
- Удаление термина.

Данные хранятся в базе данных **SQLite**, а взаимодействие с ними происходит через **FastAPI**. Валидация входных данных осуществляется с помощью **Pydantic**.

## Развертывание

### 1. Установка зависимостей

Для начала, установи Docker и Docker Compose на свою систему. Если у тебя их еще нет, следуй инструкциям на официальных сайтах:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 2. Сборка и запуск приложения

Для сборки и запуска приложения с использованием **Docker Compose**, выполни следующие шаги:

#### Шаг 1: Клонировать репозиторий

```bash
git clone https://github.com/leo4135/Glossary_fastAPI.git
cd your-repository
```

#### Шаг 2: Запуск с Docker Compose

```bash
docker-compose up --build
```

Пример API запросов

    - GET /terms — Получение списка всех терминов.

    - GET /terms/{keyword} — Получение информации о конкретном термине по ключевому слову.

    - POST /terms — Добавление нового термина с описанием.

    - PUT /terms/{keyword} — Обновление существующего термина.

    - DELETE /terms/{keyword} — Удаление термина.