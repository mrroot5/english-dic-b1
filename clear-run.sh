#!/bin/bash
read -r -p "Do you want to delete the database? [Y/n]" response
response=${response,,} # tolower
echo    # (optional) move to a new line
if [[ $response =~ ^[y|yes]$ ]]
then
    echo "Delete database. . ."
    rm db.sqlite3
    echo -e "Done\n"
fi
echo "Delete migrations. . ."
rm -rf dictionary/migrations
rm -rf dictionary/__pycache__
rm -rf _autofixture
echo -e "Done\n"
echo "Create migrations and database. . ."
source virtualenv/bin/activate
./manage.py makemigrations dictionary
./manage.py migrate
echo -e "Done\n"
echo "Creamos superuser. . . "
./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '12345678a')"
echo -e "Done\n"
echo "Start"
./manage.py runserver 0.0.0.0:8000
