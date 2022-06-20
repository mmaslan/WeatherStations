import os
import json
from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

api_key = "588237482f885cef420a4fa9796cd1b9"


def save_posts(ti) -> None:
    posts = ti.xcom_pull(task_ids=['get_posts'])
    with open('C:\\Users\\marek\\Desktop\\Data\\posts.json', w) as f:
        json.dump(posts[0], f)


with DAG(
        dag_id='weather_download',
        schedule_interval='@hourly',
        start_date=datetime(2022, 6, 25),
        catchup=False,
) as dag:
    task_is_api_active = HttpSensor(
        task_id='is_api_active',
        http_conn_id='api_posts',
        endpoint='posts/',
        method='GET',
        response_filter=lambda response: json.loads(response.text),
        log_response=True
    )

    task_save=PythonOperator(
        task_id='save_posts',
        python_callable=save_posts
    )