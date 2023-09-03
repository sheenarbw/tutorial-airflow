"""
demonstrate:
- refreshing the dag file
- dag files must be quick
- when are things printed to the console versus logs
- logging.* versus print 

Command-line demo:

airflow dags reserialize
airflow dags report
airflow dags list-import-errors

airflow dags test dag_1
airflow tasks test dag_1 task1 2023-01-01
python airflow_home/dags/dag_1.py
"""

from datetime import timedelta

from airflow.decorators import task, dag
import pendulum
import logging


@dag(
    schedule=timedelta(days=1),
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["tutorial"],
    default_args={},
)
def dag_2():
    @task()
    def task1():
        print("Hello from task 1")

    @task()
    def task2():
        logging.info("Hello from task 2")

    task1() >> task2()


dag_instance = dag_2()


if __name__ == "__main__":
    dag_instance.test()
