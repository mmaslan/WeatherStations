import os
import json
import statistics

import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

day = datetime.today().strftime("%m%d20%y")
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H:%M")


def get_weather():
    parameters = {'q': 'Gdansk', 'appid': '588237482f885cef420a4fa9796cd1b9'}

    result = requests.get('http://api.openweathermap.org/data/2.5/weather?', parameters)

    if result.status_code == 200:
        json_data = result.json()

        createDirectory()

        filename = 'data//weather_data.json'

        with open(filename, 'w') as file:
            print(filename)
            json.dump(json_data, file)
            print(json_data)
            print("closing file...")

    else:
        print("Error in Api Call")


def createDirectory():
    dirName = 'data'

    if not os.path.exists(dirName):
        try:
            os.makedirs(dirName)
            print('Directory', dirName, 'Created')

        except FileExistsError as fe:
            print('Error: ', fe)
            print('Directory', dirName, 'already exists')


def measure_mean():
    with open('C:\\Users\\marek\\Desktop\\WeatherStationsTest\\dags\\data\\weather_data.json', 'r') as file2:
        data = json.load(file2)
        main = (data['main'])
        pressure = (main['pressure'])
        print(f'Pressure is: {pressure}')

        pressure_data = [1000, 1001, 1002]
        pressure_data.append(pressure)
        print(pressure_data)
        mean_pressure = statistics.mean(pressure_data)
        print(f'Mean pressure is: {mean_pressure}')


if __name__ == '__main__':
    get_weather()
    measure_mean()

dag = DAG(
    dag_id='weather_report',
    start_date=datetime(2022, 6, 22),
    schedule_interval='@hourly')

task1 = PythonOperator(
    task_id='get_weather',
    python_callable=get_weather,
    dag=dag
)

task2 = PythonOperator(
    task_id="measure_mean",
    python_callable=measure_mean,
    dag=dag
)

task1 >> task2