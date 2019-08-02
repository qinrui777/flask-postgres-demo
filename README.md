### 01. Set up postgres
```bash
$ docker run --name flask-postgres-demo \
-e POSTGRES_PASSWORD=123456 \
-p 5432:5432 \
-d postgres:9.6.10-alpine
```

```bash
➜  flask-postgres-demo git:(master) ✗ docker exec -it flask-postgres-demo bash
bash-4.4# psql -U postgres
psql (9.6.10)
Type "help" for help.

postgres=# create database flask_demo
```

###  02.Set up Virtual Env and run app.py

clone the project to your local path

`git clone https://github.com/qinrui777/flask-postgres-with-SQLAlchemy.git && cd flask-postgres-with-SQLAlchemy.git `

create a virtual env ,named *venv*  

`virtualenv venv`

activate virtual env

`source venv/bin/activate`

install dependency from requirements.txt

`(venv) ➜  flask-postgres-demo git:(master)  pip install -r requirements.txt`

start application  

`(venv) ➜  flask-postgres-demo git:(master) ✗ python app.py`

### 
