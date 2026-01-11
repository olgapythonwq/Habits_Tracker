# Habits Tracker

A backend service for tracking useful habits inspired by James Clear's book "Atomic Habits".
This project was developed as a course final assignment and represents a REST API for an SPA application with habit reminders via Telegram.

## Content
[Features](#Features)  
[Tech Stack](#Tech Stack)  
[Installation and Running the Project (from scratch)](#Installation and Running the Project (from scratch))  
[API Documentation](#API Documentation)  
[Authentication (JWT)](#Authentication (JWT))  
[Celery and Background Tasks](#Celery and Background Tasks)  
[Telegram Notifications](#Telegram Notifications)  
[Testing](#Testing)  
[Code Quality](#Code Quality)  
[Permissions](#Permissions)  
[Project Status](#Project Status)  
[Author](#Author)

## <a id="title1">Features</a>
- User registration and authentication (JWT)
- CRUD operations for habits
- Public and private habits
- Business logic validators for habits
- Habit reminders via Telegram
- Asynchronous tasks (Celery + Redis)
- API documentation (Swagger / drf-spectacular)
- Test coverage >=80%
- Code style compliance (flake8)

## <a id="title1">Tech Stack</a>
- Python 3.13+
- Django 6
- Django REST Framework
- Simple JWT
- PostgreSQL
- Celery
- Redis
- django-celery-beat
- Telegram Bot API
- drf-spectacular
- Poetry
- Pytest
- Flake8

## <a id="title1">Installation and Running the Project (from scratch)</a>
1. Clone the repository
   ```bash
   git clone https://github.com/olgapythonwq/Habits_Tracker.git
   ```
2. Install dependencies
   ```bash
   poetry install
   ```
3. Activate the virtual environment
   ```bash
   poetry run bash
   ```
4. Create .env file in the project root
   ```bash
   SECRET_KEY=your-secret-key
   
   DJANGO_SETTINGS_MODULE=config.settings.dev
   
   DB_NAME=habits
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=localhost
   DB_PORT=5432
   
   JWT_ACCESS_LIFETIME_MINUTES=15
   JWT_REFRESH_LIFETIME_DAYS=1
   
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   
   REDIS_HOST=localhost
   REDIS_PORT=6379
   REDIS_BROKER_DB=0
   REDIS_RESULT_DB=1
   ```
5. Apply migrations
   ```bash
   python manage.py migrate
   ```
6. Create superuser
   ```bash
   python manage.py createsuperuser
   ```
7. Run Django development server
   ```bash
   python manage.py runserver
   ```      
   
## <a id="title1">API Documentation</a>
Swagger UI is available at:
[http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)

## <a id="title1">Authentication (JWT)</a>
Obtain access and refresh tokens:
   ```bash
     POST /api/token/
   ```  
Refresh access token:
   ```bash
     POST /api/token/refresh/
   ```  

## <a id="title1">Celery and Background Tasks</a>
Start Redis
Redis must be running locally

Start Celery worker (Windows)
   ```bash
     celery -A config worker -l info --pool=solo
   ```  
Start Celery Beat
   ```bash
     celery -A config beat -l info
   ``` 

## <a id="title1">Telegram Notifications</a>
- User connects to the Telegram bot
- chat_id is stored in the user profile
- Celery sends habit reminders at the schedules time

## <a id="title1">Testing</a>
Run all tests:
   ```bash
     pytest
   ``` 
Run tests with coverage report:
   ```bash
     pytest --cov
   ``` 
Test coverage is >=80%

## <a id="title1">Code Quality</a>
   ```bash
     flake8
   ```
Result: 100% (migrations excluded)

## <a id="title1">Permissions</a>
- Users can manage only their own habits
- Public habits are available read-only for all authenticated users
- All endpoints are protected with JWT and custom permissions

## <a id="title1">Project Status</a>
- [x] Completed
- [x] All acceptance criteria met
- [x] Ready for review

## <a id="title1">Author</a>
Olga
