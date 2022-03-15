#!/bin/sh

nginx -g "pid $(pwd)/nginx.pid;"
gunicorn --config=gunicorn.conf.py app.main:app
