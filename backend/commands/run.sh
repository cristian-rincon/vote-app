#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

DJANGO_MANAGER=backend/manage.py

echo "Apply database migrations"
python $DJANGO_MANAGER migrate

echo "Collect static files"
python $DJANGO_MANAGER collectstatic --noinput


echo "Run server"
python $DJANGO_MANAGER runserver 0.0.0.0:8000