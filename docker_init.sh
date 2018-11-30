#!/bin/sh

mkdir -p media
cd media
umask 011
cd ..

pipenv run gunicorn -b 0.0.0.0:8000 senne.wsgi
