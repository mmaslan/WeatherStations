import os
import json
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

dag = DAG(
    dag_id='weather_load_dag',
    # default_args=default_args,
    start_date=datetime(2022, 6, 24),
    schedule_interval='@hourly'
)

task1 = BashOperator(
    task_id='get_weather',
    dag=dag
)

task2 = PythonOperator(
    task_id='transform_data',
    provide_context=True,
    dag=dag
)

task1 >> task2
