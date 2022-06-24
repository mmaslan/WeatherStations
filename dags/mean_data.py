import os
import json
import statistics
from datetime import datetime

day = datetime.today().strftime("%m%d20%y%H%M")


def measure_mean(city):
    filename = f'data/weather_{city}_{day}.json'
    with open(os.path.join(filename), 'r') as file2:
        data = json.load(file2)
        main = (data['main'])
        pressure = (main['pressure'])
        print(f'Pressure is: {pressure}')

        pressure_file = f'data/pressure_{city}.json'
        with open(os.path.join(pressure_file), 'r') as pfile:
            avg_pressure = json.load(pfile)
            print(f'Average pressure is: {avg_pressure}')
            data_to_calculate = (avg_pressure, pressure)
            mean_pressure = statistics.mean(data_to_calculate)

            with open(pressure_file, 'w') as data_file:
                print(f'Mean pressure: {mean_pressure}')
                json.dump(mean_pressure, data_file)
