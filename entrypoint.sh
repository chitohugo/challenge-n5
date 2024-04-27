#!/bin/sh
set -e

python manage.py makemigrations traffic_violations
python manage.py migrate

python manage.py loaddata fixtures/MOCK_DATA_PERSON.json
python manage.py loaddata fixtures/MOCK_DATA_MAKE.json

python manage.py runserver 0.0.0.0:8000