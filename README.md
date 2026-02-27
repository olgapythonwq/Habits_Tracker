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
[Remote Server Setup and Application Deployment](#Remote Server Setup and Application Deployment)  
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

## <a id="title1">Remote Server Setup and Application Deployment</a>
1. Prepare the Server
   - Install Docker and Docker Compose:
   ```bash
      sudo apt update
      sudo apt install -y docker.io docker-compose
      sudo systemctl enable --now docker
   ```
   - Create a project directory:
   ```bash
      mkdir ~/Habits_Tracker
      cd ~/Habits_Tracker
   ```
   - Set up SSH access for GitHub Actions:
   1) Add the public key from SERVER_SSH_KEY to ~/.ssh/authorized_keys on the server. Test the connection:
   ```bash
      ssh user@server_ip
   ```
2. Configure GitHub Actions Secrets
- Add the following secrets in your GitHub repository:

| Secret Name | Value                    |  
| ----------- |--------------------------| 
| SECRET_KEY    | Django SECRET_KEY        | 
| DOCKERHUB_USERNAME  | Docker Hub username      |
| DOCKERHUB_TOKEN   | Docker Hub access token  | 
| SERVER_SSH_KEY    | Private SSH key for server access        | 
| SERVER_USER  | Server user     |
| SERVER_IP   | Server IP address  | 

3. Run the Workflow Locally via GitHub
- Create and switch to the develop branch:
   ```bash
      git checkout -b develop
   ```
  - Commit and push changes: 
  ```bash
     git add .
     git commit -m "Feature: CI/CD workflow test"
     git push origin develop
   ```
- GitHub Actions will automatically run the workflow:
  1) Test – runs pytest to verify code.
  2) Build – builds Docker images for all services.
  3) Deploy – deploys the application to the server.
  4) The workflow is configured to deploy only on push or pull request to the develop branch.

4. Verify Deployment
- Connect to the server via SSH:
   ```bash
      ssh user@server_ip
   ```
- Check Docker containers:
   ```bash
      docker compose ps
   ```
- Ensure all services (web, nginx, celery, redis, db) are running. 
- Open the server's public IP in a browser — your site should be live.

5. Updating the Application
- Any changes pushed to develop are automatically built and deployed via the workflow. 
- To manually update:
   ```bash
      ssh user@server_ip
      cd ~/Habits_Tracker
      docker compose pull
      docker compose up -d --remove-orphans
      docker image prune -f
   ```

## <a id="title1">Project Status</a>
- [x] Completed
- [x] All acceptance criteria met
- [x] Ready for review

## <a id="title1">Author</a>
Olga
