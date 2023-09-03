from airflow.models.xcom import BaseXCom
from pathlib import Path
import json
import logging


STORAGE_PATH = Path("gitignore/xcom_storage")


class SillyBackend(BaseXCom):
    """
    This is silly because Tasks don't share a filesystem. It's just here to demonstrate how you can make your own custom xcom backend.
    """

    @staticmethod
    def serialize_value(
        value,
        key=None,
        task_id=None,
        dag_id=None,
        run_id=None,
        map_index=None,
        **kwargs,
    ):
        file_path = STORAGE_PATH / f"{dag_id}/{task_id}/{key}.json"
        file_path = file_path.resolve()
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w") as f:
            json.dump(value, f, indent=4, sort_keys=True)

        logging.info(f"file_path = {file_path}")
        result = BaseXCom.serialize_value(str(file_path))
        return result

    @staticmethod
    def deserialize_value(result):
        file_path = BaseXCom.deserialize_value(result)
        with open(file_path) as f:
            data = json.load(f)
        return data

    def orm_deserialize_value(self):
        """display this value on the frontend"""
        file_path = BaseXCom._deserialize_value(self, True)
        with open(file_path) as f:
            data = f.read()
        if len(data) > 20:
            return data[:20] + "..."
        return data
