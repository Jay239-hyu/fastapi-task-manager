
# FastAPI-Task-Manager
Task Manager backend built with FastAPI, fully containerized using Docker, with Nginx as a reverse proxy. Designed for scalability and production readiness.


# Features
CRUD Operations

JWT Token Authentication

Fully Dockerized system

Nginx reverse proxy

Scalable architecture

SSL support (planned)


# Tech Stack
Backend

    FastAPI

    Python

Database

    PostgreSQL

Web Server

    Nginx

DevOps

    Docker & Docker Compose




# Project Structure
```text
task-manager/
│
├── alembic/
├── app/
│   ├── core/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── db.py
│   └── main.py
│
├── nginx/
├── .dockerignore
├── .gitignore
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── requirements.txt
└── README.md
```


# Getting Started   

Prerequisites

    Docker

    Docker Compose

    Git

    Postman or Swagger (for API testing)

Clone The Repository

    git clone https://github.com/your-username/taskmanager.git
    cd taskmanager

Environment Setup (example values — adjust as needed)

    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=taskmanager

    DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/taskmanager

    SECRET_KEY=your_generated_secret_key
    ALGORITHM=HS256
    EXP_TIME_IN_SEC=3600

    Generate secret key using Python:

        python -c "import secrets; print(secrets.token_hex(32))"


Run the Application

    Start all services (Postgres, FastAPI, Nginx):

        docker compose up --build

    Detached mode:

        docker compose up -d --build

    Verify Containers:

        docker compose ps

Access the Application

    🌐 API Base URL: http://localhost
    📚 Swagger UI: http://localhost/docs
    🔍 ReDoc: http://localhost/redoc

Health Check

    GET /health

    Expected Response:
        {
            "status": "OK"
        }

Stop the Application

    docker compose down

API Testing

    You can test APIs using:

    Swagger UI (recommended)

    Postman collection

# API Documentation

Available via Swagger at:

    http://localhost/docs



# Testing
Pending

# Deployment
Pending

# Contributing 
Currently not open for contributions.

# License
License not specified yet.

# Maintainers
Jay Valand 


