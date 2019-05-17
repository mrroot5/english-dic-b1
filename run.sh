#!/bin/bash
echo "Activate enviorement"
source venv/bin/activate
echo "Database changes"
./manage.py makemigrations dictionary
./manage.py migrate
echo "Start"
./manage.py runserver 0.0.0.0:8000
