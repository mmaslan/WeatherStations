import os
import json
import statistics
import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

day = datetime.today().strftime("%m%d20%y%H%M")


def get_weather(city):
    parameters = {f'q': {city}, 'appid': '588237482f885cef420a4fa9796cd1b9'}

    result = requests.get('http://api.openweathermap.org/data/2.5/weather?', parameters)

    if result.status_code == 200:
        json_data = result.json()

        createDirectory()

        filename = f'data//weather_{city}_{day}.json'

        with open(filename, 'w') as file:
            print(f"Weather data in {city}:")
            json.dump(json_data, file)
            print(json_data)

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


def measure_mean(city):
    with open(f'C:\\Users\\marek\\Desktop\\WeatherStationsTest\\dags\\data\\weather_{city}_{day}.json', 'r') as file2:
        data = json.load(file2)
        main = (data['main'])
        pressure = (main['pressure'])
        print(f'Pressure is: {pressure}')

        pressure_data = [1000, 1001, 1002]
        pressure_data.append(pressure)
        print(pressure_data)
        mean_pressure = statistics.mean(pressure_data)
        print(f'Mean pressure is: {mean_pressure}')


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


dag = DAG(
    dag_id='weather_report',
    start_date=datetime(2022, 6, 22),
    schedule_interval='@hourly'
)

task1 = PythonOperator(
    task_id='weather_gdansk',
    python_callable=weather_gdansk,
    dag=dag
)

task2 = PythonOperator(
    task_id="measure_mean",
    python_callable=weather_warsaw,
    dag=dag
)

task3 = PythonOperator(
    task_id="mean_gdansk",
    python_callable=mean_gdansk,
    dag=dag
)

task4 = PythonOperator(
    task_id="mean_warsaw",
    python_callable=mean_warsaw,
    dag=dag
)

task1 >> task2
task3 >> task4