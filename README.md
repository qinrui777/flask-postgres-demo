### Set up postgres


$ docker run --name flask-postgres-demo \
-e POSTGRES_PASSWORD=123456 \
-p 5432:5432 \
-d postgres:9.6.10-alpine


➜  flask-postgres-demo git:(master) ✗ docker exec -it flask-postgres-demo bash


postgres=# create database flask_demo




### 