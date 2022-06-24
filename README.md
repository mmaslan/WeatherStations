# WeatherStations
# Installation guide

**Create virtual environment:**

virtualenv venv

**Apache Airflow installation**

pip install "apache-airflow[celery]==2.3.2" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.10.txt"

**Installation of docker-compose.yaml**

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.3.2/docker-compose.yaml'

**Initialize the database**

docker-compose up airflow-init

