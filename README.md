# Flask Expense Tracker API

REST API для відстеження особистих витрат, побудований на Flask з JWT-аутентифікацією та документацією Swagger.

## Технології

- **Flask 3.1.2** - веб-фреймворк
- **SQLAlchemy 2.0.45** - ORM для роботи з базою даних
- **Flask-JWT-Extended 4.7.1** - JWT-аутентифікація
- **Flask-Migrate 4.1.0** - міграції бази даних через Alembic
- **Marshmallow 4.2.0** - серіалізація/валідація даних
- **Flask-Swagger-UI 5.21.0** - інтерактивна документація API
- **Gunicorn 23.0.0** - WSGI-сервер для production
- **Pytest 9.0.2** - тестування

## Функціональність

- Реєстрація та автентифікація користувачів
- JWT-токени для захищених ендпоінтів
- CRUD-операції для витрат
- Автоматична документація API через Swagger
- Міграції бази даних
- Docker-підтримка
- CI/CD через GitHub Actions

## Швидкий старт

### Локальна розробка

1. Клонуйте репозиторій:
```bash
git clone https://github.com/IlyaOriekhov/flaskapp.git
cd flaskapp
```

2. Створіть віртуальне середовище:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# або
venv\Scripts\activate  # Windows
```

3. Встановіть залежності:
```bash
pip install -r requirements.txt
```

4. Запустіть міграції:
```bash
flask db upgrade
```

5. Запустіть сервер:
```bash
flask run
# або для production
gunicorn wsgi:app
```

### Docker

```bash
docker build -t flaskapp .
docker run -p 5000:5000 flaskapp
```

## API Endpoints

### Аутентифікація
- `POST /api/register` - реєстрація користувача
- `POST /api/login` - вхід (отримання JWT-токену)

### Витрати
- `GET /api/expenses` - список всіх витрат
- `POST /api/expenses` - створення нової витрати
- `GET /api/expenses/{id}` - деталі витрати
- `PUT /api/expenses/{id}` - оновлення витрати
- `DELETE /api/expenses/{id}` - видалення витрати

Всі ендпоінти витрат вимагають JWT-токен в заголовку `Authorization: Bearer <token>`.

## Документація Swagger

Після запуску застосунку документація доступна за адресою:
```
http://localhost:5000/swagger
```

## Структура проекту

```
flaskapp/
├── app/
│   ├── __init__.py          # Ініціалізація Flask app
│   ├── config.py            # Конфігурація
│   ├── db.py                # Моделі бази даних
│   ├── user.py              # Ендпоінти користувачів
│   ├── expense.py           # Ендпоінти витрат
│   ├── jwt.py               # JWT конфігурація
│   ├── schemas.py           # Marshmallow схеми
│   ├── swagger_bp.py        # Swagger blueprint
│   └── swagger_utils.py     # Swagger утиліти
├── migrations/              # Міграції Alembic
├── tests/                   # Тести
├── Dockerfile              # Docker конфігурація
├── requirements.txt        # Python залежності
└── wsgi.py                # WSGI entry point
```

## Тестування

```bash
pytest
```

## Змінні середовища

- `DATABASE_URL` - URL бази даних (за замовчуванням SQLite)
- `SECRET_KEY` - секретний ключ для JWT
- `JWT_SECRET_KEY` - окремий ключ для JWT-токенів
