"""
demonstrate:
- task dependencies and taskflow api
- look at XCOM values in gui

Command-line demo:

airflow dags test dag_2
python airflow_home/dags/dag_2.py

airflow tasks test dag_2 task1 2023-01-01

airflow tasks test dag_2 task2 2023-01-01
pay attention to arg value. How do we set it?
"""

from datetime import timedelta
from airflow import DAG
from airflow.decorators import task
import pendulum
import logging

with DAG(
    "dag_3",
    description="DAG 2",
    schedule=timedelta(days=1),
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["tutorial"],
) as dag:

    @task()
    def task1():
        return 123

    @task(multiple_outputs=True)
    def task2(arg):
        logging.info("Hello from task 2")
        logging.info(f"arg: {arg}")
        return {"arg": arg, "arg2": 456}

    @task()
    def task3(arg, arg2):
        logging.info("Hello from task 3")
        logging.info(f"arg: {arg}")
        logging.info(f"arg2: {arg2}")

    x = task1()
    y = task2(x)
    task3(y["arg"], y["arg2"])

if __name__ == "__main__":
    dag.test()
