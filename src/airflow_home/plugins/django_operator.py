import os, sys
from pathlib import Path
from airflow.decorators import task


def django_connect(app_path, settings_module):
    # Add Django project root to path
    sys.path.append(str(app_path))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    from django.apps import apps
    from django.conf import settings

    apps.populate(settings.INSTALLED_APPS)


def make_django_decorator(app_path, settings_module):
    def django_task(task_id: str = None, *args, **kwargs):
        def django_task_decorator(fn):
            @task(task_id=task_id or fn.__name__, *args, **kwargs)
            def new_fn(*args, **kwargs):
                django_connect(app_path, settings_module)
                return fn(
                    *args,
                )

            return new_fn

        return django_task_decorator

    return django_task


django_project_1_task = make_django_decorator(
    app_path="/home/sheena/workspace/airflow-tutorial/src/django_project_1",
    settings_module="django_project_1.settings",
)


django_project_2_task = make_django_decorator(
    app_path="/home/sheena/workspace/airflow-tutorial/src/django_project_2",
    settings_module="django_project_2.settings",
)
