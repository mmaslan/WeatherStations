import airflow
from airflow import DAG
from airflow.operations.bash import BashOperator
from airflow.operations.python import PythonOperator


dag = DAG(
    dag_id='download_weather_data',
    start_date=now,
    schedule_interval='@hourly'
)