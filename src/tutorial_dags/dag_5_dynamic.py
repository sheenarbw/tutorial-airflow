"""
# Demonstrate:

- change DAG_COUNT number

# Docs:

https://airflow.apache.org/docs/apache-airflow/stable/howto/dynamic-dag-generation.html

# Questions

- dynamic dags are created according to some data or information. Where can that come from? Here we hardcoded things and just looped over a range. Can you think of something more realistic? 
- task2 takes in 2 arguments, where do they come from?
"""

from datetime import timedelta

from airflow.decorators import task, dag
import pendulum
import logging

DAG_COUNT = 1

dags = []

for dag_number in range(DAG_COUNT):

    @dag(
        dag_id=f"dag_5_{dag_number}",
        schedule=timedelta(days=1),
        start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
        catchup=False,
        tags=["tutorial"],
        default_args={},
    )
    def dag_5():
        @task()
        def task1():
            logging.info(f"Hello from task 1")
            logging.info(f"dag_number = {dag_number}")
            return dag_number

        y = task1()

        task_2_returns = []

        for n in range(dag_number + 1):

            @task(task_id=f"task2_{n}")
            def task2(y, n):
                logging.info(f"Hello from task 2")
                logging.info(f"dag_number = {dag_number}")
                logging.info(f"y = {y}")
                logging.info(f">>> n = {n}")
                return n

            task_2_returns.append(task2(y, n))

        @task()
        def task3(*args):
            logging.info(f"Hello from task 3")
            logging.info(f"dag_number = {dag_number}")
            logging.info(f"args = {args}")

        task3(*task_2_returns)

    dags.append(dag_5())


if __name__ == "__main__":
    for dag in dags:
        dag.test()
