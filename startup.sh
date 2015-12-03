#!/usr/bin/env bash

#python manage.py create_pdf

gunicorn -c /config/gunicorn.conf wsgi:app
