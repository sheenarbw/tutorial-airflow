# Django setup

This tutorial will cover how you can connect Airflow to Django. So let's get that set up.

### 1. Make sure your database runs

Our Django projects are going to be plugging into some Postgres databases. We'll use Docker and docker-compose to make life easy.

```
cd src/database
docker-compose up
```

If you take a look at the docker-composition you'll see that we have made one user, `pguser`. It has the password `password`. There are 4 databases that it has access to:

- db1: This is used for django_project_1
- test_db1: This will be used by unit tests running in django_project_1
- db2: This is used for django_project_2
- test_db2: This will be used by unit tests running in django_project_2

You will need to have this docker-composition running any time you want to access the django-project databases in any way. 

### 2. Add fake data into Django DBs

Make sure your database is running as per 4, then in a separate terminal:

Activate your virtual env then: 

```
cd src/django_project_1
python manage.py migrate 
python manage.py create_demo_data

cd ../django_project_2
python manage.py migrate 
python manage.py create_demo_data
```
