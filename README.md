# 🚀 FastAPI Task Manager (Production Ready)

A fully functional **Task Manager API** built using FastAPI, deployed with Docker, connected to Supabase (PostgreSQL), and integrated with a live frontend (Vercel).

👉 Designed with **real-world deployment, scalability, and clean architecture** in mind.

---

# ✨ Features

* 🔐 JWT Authentication (Login system)
* 📝 Full CRUD (Create, Read, Update, Delete tasks)
* 🧠 Clean layered architecture (routers → services → db)
* 🐳 Dockerized backend
* ☁️ Live deployment (Render)
* 🌐 Frontend integration (Vercel)
* 🗄️ PostgreSQL (Supabase cloud DB)
* ⚙️ Alembic migrations
* 🛡️ CORS configured for frontend communication

---

# 🧱 Tech Stack

## Backend

* FastAPI
* Python 3.11

## Database

* PostgreSQL (Supabase)

## DevOps

* Docker
* Render (Backend hosting)
* Vercel (Frontend hosting)

## Tools

* Alembic (migrations)
* Axios (frontend API calls)

---

# 📂 Project Structure

```text
task-manager/
│
├── alembic/
├── app/
│   ├── core/        # config, settings, logging
│   ├── models/      # database models
│   ├── routers/     # API routes
│   ├── schemas/     # request/response schemas
│   ├── services/    # business logic
│   ├── db.py
│   └── main.py
│
├── nginx/           # (used for local/docker setup)
├── .env.dev
├── .env.production
├── .env.vps
├── Dockerfile
├── entrypoint.sh
├── requirements.txt
└── README.md
```

---

# ⚙️ Environment Setup

## 🔹 Local Development (.env.dev)

```env
DATABASE_URL=your_local_db_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
EXP_TIME_IN_SEC=3600
ENV=dev
```

---

## 🔹 Production (Render)

👉 Render dashboard me manually set kare:

```env
DATABASE_URL=your_supabase_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
EXP_TIME_IN_SEC=3600
ENV=production
```

---

## ⚠️ Important

* `.env.production` & `.env.vps` future use ke liye hain (VPS / advanced setup)
* Current deployment → Render ENV variables use karta hai

---

# 🐳 Run Locally (Docker)

## 1. Clone Repo

```bash
git clone https://github.com/your-username/taskmanager.git
cd taskmanager
```

---

## 2. Run Containers

```bash
docker compose up --build
```

Detached mode:

```bash
docker compose up -d --build
```

---

## 3. Check Running Containers

```bash
docker compose ps
```

---

# 🌐 Access API (Local)

* API: http://localhost
* Swagger: http://localhost/docs
* ReDoc: http://localhost/redoc

---

# ☁️ Live Deployment

## 🔹 Backend (Render)

👉 Live URL:

```
https://task-manager-backend-o278.onrender.com
```

---

## 🔹 Frontend (Vercel)

👉 Connected with backend using Axios

---

# 🔐 Authentication Flow

1. User login → `/auth/login`
2. JWT token generate
3. Token stored in frontend (localStorage)
4. All protected APIs use:

```http
Authorization: Bearer <token>
```

---

# 🧪 Testing

* Swagger UI (recommended)
* Postman

---

# 🛠️ Common Issues & Fixes

## ❌ CORS Error

👉 Fix:

* frontend domain add karo (without trailing `/`)

---

## ❌ DB Connection Error

👉 Fix:

* correct Supabase URL use karo
* session pooler use karo

---

## ❌ Login working in Swagger but not frontend

👉 Fix:

* Axios baseURL check karo
* request body match karo (username/email)

---

## ❌ Container stuck on startup

👉 Fix:

* `pg_isready` remove karo (external DB case)

---

# 🧠 Key Learnings

* Deployment ≠ just running code
* Logs are your best friend
* CORS is the most common issue
* ENV handling is critical in production

---

# 🚀 Future Improvements

* Refresh token system
* Role-based auth
* Rate limiting
* Redis caching
* VPS deployment (Docker + Nginx + SSL)

---

# 👨‍💻 Maintainer

**Jay Valand**

---

# 🏁 Final Note

👉 This project is not just a CRUD app —
👉 It is a **complete production deployment journey**

Built with real debugging, real problems, and real solutions 💯

---
