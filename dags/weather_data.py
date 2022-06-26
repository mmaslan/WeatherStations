import json
import requests
from datetime import datetime

day = datetime.today().strftime("%m%d20%y%H")


def get_weather(city):
    parameters = {f'q': {city}, 'appid': '588237482f885cef420a4fa9796cd1b9'}

    result = requests.get('http://api.openweathermap.org/data/2.5/weather?', parameters)

    if result.status_code == 200:
        json_data = result.json()

        filename = f'weather_{city}_{day}.json'
        with open(filename, 'w') as file:
            print(f"Weather data in {city}:")
            json.dump(json_data, file)
            print(json_data)
    else:
        print("Error in Api Call")
