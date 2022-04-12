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

# Check if DATABASE variable is set and if it is, use $PORT variable
database_variable(){
    if [ -z "$DATABASE" ]; then
        echo "DATABASE variable is not set, running server on port 8000"
        python $DJANGO_MANAGER runserver 0.0.0.0:8000
    else
        echo "DATABASE variable is set, running server on port $PORT"
        python $DJANGO_MANAGER runserver 0.0.0.0:$PORT
    fi
}

database_variable