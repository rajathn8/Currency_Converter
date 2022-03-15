#!/bin/sh

nginx -g "pid $(pwd)/nginx.pid;"
cd app/
gunicorn --config=./gunicorn.conf.py main:app
