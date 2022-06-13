# README

Anovis Cloud Agent Controller Implementation based on ACA-PY

## RUN ACA-PY

./scripts/run_docker start --inbound-transport http 0.0.0.0 8030 --outbound-transport http --admin 0.0.0.0 8040 --admin-insecure-mode --debug --log-level DEBUG

## Django

install django: `pip install django`
create django project: `django-admin startproject projectname`
create app inside project: `python3 manage.py startapp appname`
run django server: `python3 manage.py runserver` -> Open Browser and navigate to http://127.0.0.1:8000/api

Application code is served by files like api/views.py.
URLs are defined in urls.py files. Root urls file is controller/urls.py.
