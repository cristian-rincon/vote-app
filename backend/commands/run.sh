#!/bin/bash

DJANGO_MANAGER=backend/manage.py

echo "Collect static files"
python $DJANGO_MANAGER collectstatic --noinput

echo "Apply database migrations"
python $DJANGO_MANAGER migrate

echo "Run server"
python $DJANGO_MANAGER runserver 0.0.0.0:8000