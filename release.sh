#!/bin/bash
python manage.py compress
python manage.py collectstatic
python manage.py createcachetable
python manage.py makemigrations
python manage.py migrate