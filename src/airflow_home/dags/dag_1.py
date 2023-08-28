"""
demonstrate:
- refreshing the dag file: airflow dags reserialize
- when are things printed to the console versus logs
- logging.* versus print 


Command-line demo:

airflow dags reserialize
airflow dags list-import-errors

airflow test dag_1 task1 2023-01-01
python airflow_home/dags/dag_1.py

"""

from datetime import timedelta
from airflow import DAG

from airflow.decorators import task
import pendulum
import logging

with DAG(
    "dag_1",
    description="DAG 1",
    schedule=timedelta(days=1),
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["tutorial"],
) as dag:
    print("xxxxxxxxxxxx")

    @task()
    def task1():
        print("Hello from task 1")

    @task()
    def task2():
        logging.info("Hello from task 2")

    task1() >> task2()

if __name__ == "__main__":
    dag.test()
