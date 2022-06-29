# README

Anovis Cloud Agent Controller Implementation based on ACA-PY

## RUN Indy Ledger (VON-Network)
The VON-Network repo provides a simple indy node cluster setup for local development.

`https://github.com/bcgov/von-network/blob/main/docs/UsingVONNetwork.md`

``
git clone https://github.com/bcgov/von-network
cd von-network

./manage build
./manage start --logs
``

Ledger Browser: `http://localhost:9000/`

## RUN Indy Node
`./pool_start.sh [number of nodes in pool] [IP addresses of nodes] [number of clients] [port for the first node]`
`./pool_stop.sh [file with pool data] [pool network name]`

run with docker:
```
Start the pool of local nodes on 127.0.0.1:9701-9708 with Docker by running:

docker build -f ci/indy-pool.dockerfile -t indy_pool .
docker run -itd -p 9701-9708:9701-9708 indy_pool
```
docker network:
```
docker network create --subnet 10.0.0.0/8 indy_pool_network
docker build --build-arg pool_ip=10.0.0.2 -f ci/indy-pool.dockerfile -t indy_pool .
docker run -d --ip="10.0.0.2" --net=indy_pool_network indy_pool
```

## RUN ACA-PY

`./scripts/run_docker start --inbound-transport http 0.0.0.0 8030 --outbound-transport http --admin 0.0.0.0 8040 --admin-insecure-mode --debug --log-level DEBUG`

## RUN ACA-PY Demo

TODO: Setup demo with GENESIS_FILE

Start Aca-Py demo with docker in the background
`LEDGER_URL=http://dev.greenlight.bcovrin.vonx.io ./run_demo faber --events --no-auto --bg`

Connect terminal to docker container running in the background
`docker logs -f faber`

Admin URL (usually):  http://172.17.0.1:8021
Open in Browser to acces Swagger Interface

## Django

install django: `pip install django`
create django project: `django-admin startproject projectname`
create app inside project: `python3 manage.py startapp appname`
run django server: `python3 manage.py runserver` -> Open Browser and navigate to http://127.0.0.1:8000/api to send a GET request to test endpoint

Application code is served by files like api/views.py.
URLs are defined in urls.py files. Root urls file is controller/urls.py.
