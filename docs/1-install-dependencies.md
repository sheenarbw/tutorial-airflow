# Install dependencies

### 1. Install base software

You'll need the following:

- Docker and docker-compose: We will be using these to run some Postgres databases
- Python 3.10: Unfortunately, Airflow doesn't officially support 3.11 yet

### 2. Set up a virtual environment

In real-world projects, it's likely that Airflow and the Django projects would be developed in different places. Perhaps they would have different repos, and they would definitely have different virtual environments. We're just using one virtual environment for all of the things so we can keep things simple.

Note: Airflow does not yet support any package managers beyond pip. Eg `poetry` is not officially supported. So we are doing things in a bit of an old-school way:

```
cd src 
python3.10 -m venv venv
source venv/bin/activate 

pip install -r requirements.txt 
```

If you get an error that includes the following:

```
  ./psycopg/psycopg.h:36:10: fatal error: libpq-fe.h: No such file or directory
     36 | #include <libpq-fe.h>
```

Then you'll need to install some Postgres development headers and try again. On Ubuntu, you would do this:

```
sudo apt install libpq-dev  
```

Once you have installed the prerequisites then try `pip install -r requirements.txt` again.

### 2. Install Airflow

Airflow installation is a little bit unusual. To keep things explicit we'll do this in a separate step:

```
source venv/bin/activate # activate your venv if you haven't already

AIRFLOW_VERSION=2.7.0
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

Learn more here: https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html 