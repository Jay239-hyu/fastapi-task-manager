#!/usr/bin/env sh

set -e

echo "⏳ Waiting for Postgres..."

# wait until postgres is ready

until pg_isready -h db -p 5432 -U "$POSTGRES_USER" -d "$POSTGRES_DB"; do

  sleep 1

done

echo "✅ Postgres is ready"

echo "🚀 Running migrations..."

alembic upgrade head

echo "🔥 Starting FastAPI..."

exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
