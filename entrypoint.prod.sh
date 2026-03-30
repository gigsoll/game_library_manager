#!/usr/bin/env bash
set -e
cd /app
python manage.py collectstatic --noinput
python manage.py migrate --noinput
exec python -m gunicorn --bind 0.0.0.0:8000 game_library_manager.wsgi
