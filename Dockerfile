# Base image
FROM python:3.11-slim

# Prevent python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# System dependencies (optional but recommended)
RUN apt-get update && apt-get install -y \
    build-essential \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for caching)
COPY requirements.txt .

# Just upgrade pip to avoid old pip usage
RUN pip install --upgrade pip

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project and change script file permission
COPY . .
RUN chmod +x /app/entrypoint.sh

# Expose port
EXPOSE 8000

