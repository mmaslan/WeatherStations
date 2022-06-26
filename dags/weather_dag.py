import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from mean_data import measure_mean
from weather_data import get_weather


def weather_gdansk():
    return get_weather('Gdansk')


def weather_warsaw():
    return get_weather('Warsaw')


def mean_gdansk():
    return measure_mean('Gdansk')


def mean_warsaw():
    return measure_mean('Warsaw')


if __name__ == '__main__':
    weather_gdansk()
    weather_warsaw()
    mean_gdansk()
    mean_warsaw()


default_args = {
    "start_date": "2022-06-24",
    "depends_on_past": False,
    "retries": 10,
}

dag = DAG(
    dag_id='weather_report',
    start_date=datetime(2022, 6, 24),
    schedule_interval='@hourly',
)

task1 = PythonOperator(
    task_id='weather_gdansk',
    python_callable=weather_gdansk,
    dag=dag
)

task2 = PythonOperator(
    task_id="mean_gdansk",
    python_callable=mean_gdansk,
    dag=dag
)

task3 = PythonOperator(
    task_id="weather_warsaw",
    python_callable=weather_warsaw,
    dag=dag
)

task4 = PythonOperator(
    task_id="mean_warsaw",
    python_callable=mean_warsaw,
    dag=dag
)

task1 >> task2
task3 >> task4
