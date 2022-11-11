#!/usr/bin/env bash
set -e
python manage.py migrate --noinput
uwsgi --strict --ini /app/uwsgi/uwsgi.ini
