#!/bin/sh

nginx -g "pid $(pwd)/nginx.pid;"
cmd ls
yourfilenames=`ls *`
for eachfile in $yourfilenames
do
   echo $eachfile
done
cd app/
gunicorn --config=./gunicorn.conf.py main:app
