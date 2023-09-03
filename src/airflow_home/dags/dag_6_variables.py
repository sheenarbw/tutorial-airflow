"""
airflow variables import airflow_home/dags/dag_6_variables.json
visit: http://localhost:8080/variable/list/ 

# docs:

https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/variables.html#variables

For security purpose, you’re recommended to use the Secrets Backend for any variable that contains sensitive data.

https://airflow.apache.org/docs/apache-airflow/stable/security/secrets/secrets-backend/index.html#secrets-backend-configuration
"""

from datetime import timedelta

from airflow.decorators import task, dag
import pendulum
import logging
from airflow.models import Variable

# https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#airflow-variables
# vars = Variable.get("dag_6", deserialize_json=True)
# logging.info("=======================")
# logging.info(f"vars = {vars}")


@dag(
    schedule=timedelta(days=1),
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["tutorial"],
    default_args={},
)
def dag_6():
    @task()
    def task1():
        vars = Variable.get("dag_6", deserialize_json=True)
        logging.info(f"vars = {vars}")

    task1()


dag_instance = dag_6()

if __name__ == "__main__":
    dag_instance.test()
