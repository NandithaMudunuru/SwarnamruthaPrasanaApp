#!/bin/bash
python manage.py createcachetable
python manage.py makemigrations
python manage.py migrate