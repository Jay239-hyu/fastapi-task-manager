# Base image
FROM python:3.11-slim

# Prevent python from writing pyc files & buffering logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (better caching)
COPY requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy ONLY required backend code (avoid frontend bloat)
COPY app ./app
COPY alembic ./alembic
COPY alembic.ini .
COPY entrypoint.sh .

# Give execution permission
RUN chmod +x /app/entrypoint.sh

# Render dynamically assigns PORT → use env var
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]