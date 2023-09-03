# Airflow tutorial

As data-driven organizations grow, life gets… complicated

- Data and task pipeline requirements grow
- More data sources and sinks are added to the mix
- Tasks become dependent on each other in complicated ways
- Service level agreements need to be adhered to and monitored
- Schedules need to be maintained

![XKCD data pipelines](https://imgs.xkcd.com/comics/data_pipeline.png)

Apache Airflow, initially developed and open-sourced by those nice folks at Airbnb, solves these problems and more.

In this tutorial, we’ll be starting off by getting to grips with Airflow as a stand-alone tool, and then we’ll see how we can get it to play nicely with the Django ORM.

## Prerequisite knowledge

- No prior experience with Airflow is needed
- No prior experience with Django is needed, although it would be nice if you know a bit about ORMs

It would be useful if you are familiar with:

- Python of course
- virtual environments
- environmental variables

## Directory structure

All the code for this tutorial can be found inside the src directory. It looks like this:

```
airflow_home/
database/
django_project_1/
django_project_2/
tutorial_dags/
requirements.txt
```

- Airflow has a concept called `airflow_home`. This is where your airflow configuration and dags can be found. For now, this directory is empty. That's intentional
- database: Our Django applications will be storing their data in Postgres databases. These are defined through docker-compose
- django_project_*: We will be showing how Airflow can play nice with 2 separate Django projects. This is useful because many organizations are likely to run multiple projects
- tutorial_dags: We'll cover this later in detail :)
- requirements.txt: The usual

## Setup

By the end of this section, you will be able to run Airflow, and the Django projects will both be able to connect to Postgres databases. 


1. [Install dependencies](docs/1-install-dependencies.md)
2. [Set up Airflow](docs/2-setup-airflow.md)
2. [Set up Django](docs/3-django-setup.md)




### 5. Make sure your database runs

Our Django projects are going to be plugging into some Postgres databases. We'll use Docker and docker-compose to make life easy.

```
cd database
docker-compose up
```

If you take a look at the docker-composition you'll see that we have made one user, `pguser`. It has the password `password`. There are 4 databases that it has access to:

- db1: This is used for django_project_1
- test_db1: This will be used by unit tests running in django_project_1
- db2: This is used for django_project_2
- test_db2: This will be used by unit tests running in django_project_2

You will need to have this docker-composition running any time you want to access the django-project databases in any way. 

### 6. Add fake data into Django DBs

Make sure your database is running as per 4, then in a separate terminal:

```
source venv/bin/activate # activate your venv

cd django_project_1
python manage.py migrate 
python manage.py create_demo_data

cd ../django_project_2
python manage.py migrate 
python manage.py create_demo_data
```

### DONE!

You should be able to run the database, the django projects and `airflow standalone` without any problems. 