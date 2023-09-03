"""
# Demonstrate:

- this will fail if postgres db not running 
- django decorators are hard to reason about
- django connect method is much easier
- need to be careful how we connect to django or it breaks logging
- task5: this wont work

"""

from datetime import timedelta
from airflow import DAG

from airflow.decorators import task
import pendulum
import logging

from django_operator import (
    django_project_1_task,
    django_project_2_task,
    django_connect,
    SRC_DIRECTORY,
)

with DAG(
    "dag_4",
    description="DAG 3",
    schedule=timedelta(days=1),
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["tutorial"],
) as dag:

    @django_project_1_task()
    def task1():
        from dogs.models import Dog

        count = Dog.objects.count()
        return count

    @django_project_2_task()
    def task2():
        from cats.models import Cat

        count = Cat.objects.count()
        return count

    @task()
    def task3(arg1, arg2):
        logging.info(f"dog count: {arg1}")
        logging.info(f"cat count: {arg2}")
        return arg1 + arg2

    @task()
    def task4(arg):
        django_connect(
            app_path=SRC_DIRECTORY / "django_project_1",
            settings_module="django_project_1.settings",
        )

        from dogs.models import Dog

        first = Dog.objects.first()

        logging.info(f"total: {arg}")
        logging.info(f"Dog 1: {first.name}")

    # @task()
    # def task5():
    #     django_connect(
    #         app_path=SRC_DIRECTORY/"django_project_1",
    #         settings_module="django_project_1.settings",
    #     )
    #     from dogs.models import Dog

    #     dog = Dog.objects.first()

    #     django_connect(
    #         app_path=SRC_DIRECTORY/"django_project_2",
    #         settings_module="django_project_2.settings",
    #     )
    #     from cats.models import Cat

    #     cat = Cat.objects.first()

    #     logging.info(f"dog: {dog.name}")
    #     logging.info(f"cat: {cat.name}")

    #     dog.name = "Snoopy"
    #     dog.save()
    #     cat.name = "Garfield"
    #     cat.save()

    dogs = task1()
    cats = task2()

    total = task3(dogs, cats)
    task4(total)
    # task5()


if __name__ == "__main__":
    dag.test()
