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

- Airflow has a concept called `airflow_home`. This is where your airflow configuration and dags can be found. For now, this directory is empty. That is on purpose
- database: Our Django applications will be storing their data in Postgres databases. These are defined through docker-compose
- django_project_*: We will be showing how Airflow can play nice with 2 separate Django projects. This is useful because many organizations are likely to run multiple projects
- tutorial_dags: We'll cover this later in detail :)
- tutorial_plugins: This too
- requirements.txt: The usual

## Setup

By the end of this section, you will be able to run Airflow, and the Django projects will both be able to connect to Postgres databases. 

1. [Install dependencies](docs/1-install-dependencies.md)
2. [Set up Airflow](docs/2-setup-airflow.md)
2. [Set up Django](docs/3-django-setup.md)
