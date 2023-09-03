"""
Questions:

- which params show up in the gui? Which don't?
- which value of string_param is used in task1?
- what happens if you directly edit the generated config json in the gui so that task1_param is 20? what happens if you set extra values? 
"""

from datetime import timedelta
from airflow.decorators import task, dag
import pendulum
import logging
from airflow.models.param import Param
from airflow.operators.python import get_current_context


@dag(
    schedule=timedelta(days=1),
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["tutorial"],
    default_args={},
    params={
        "integer_param": Param(5, type="integer", minimum=3),
        "string_param": "placeholder",
    },
)
def dag_7():
    @task(
        params={
            "task1_param": 10,
            "string_param": "override",
        },
    )
    def task1():
        context = get_current_context()
        params = context.get("params")
        for k, v in params.items():
            logging.info(f"{k} = {v}")

    task1()


dag_7()
