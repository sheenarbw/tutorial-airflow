# Airflow tutorial

Follow me on the socials if you want more of this kind of thing:

- [Mastadon: @sheenarbw](https://mastodon.social/@sheenarbw)
- [Fossdon: @sheena](https://fosstodon.org/@sheena)
- [Twitter: @sheena_oconnell](https://twitter.com/sheena_oconnell)

## Introduction

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
- Virtual environments
- Environmental variables

## Directory structure

All the code for this tutorial can be found inside the src directory. It looks like this:

```
airflow_home/
database/
django_project_1/
django_project_2/
tutorial_dags/
tutorial_plugins/
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

Note that getting Airflow to work on Windows is a bit painful. If you are using a windows machine please try use Linux subsystem for windows, or a Linux VM or container.

1. [Install dependencies](docs/1-install-dependencies.md)
2. [Set up Airflow](docs/2-setup-airflow.md)
2. [Set up Django](docs/3-django-setup.md)

## How to run the tutorial

If you are presenting this to an audience then:

1. Make use of the presentation. It was created using reveal.js
2. When the presentation references a dag (eg DAG 1) then copy that dag into the airflow_home/dags directory
3. When it references a plugin then copy that across into the plugins directory 

Each dag file has a bunch of questions and notes at the top. If you can answer those questions then you are good.

