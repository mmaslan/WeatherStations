import os
import json
import requests
from datetime import datetime


def get_weather():
    parameters = {'q': 'Gdansk', 'appid': '588237482f885cef420a4fa9796cd1b9'}

    result = requests.get('http://api.openweathermap.org/data/2.5/weather?', parameters)

    if result.status_code == 200:
        json_data = result.json()

        createDirectory()

        filename = 'data/' + str(datetime.now().date) + '.json'

        with open(filename, 'w') as file:
            print(filename)
            json.dump(json_data, file)
            print(json_data)
            print("closing file . . . ")

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


if __name__ == '__main__':
    get_weather()