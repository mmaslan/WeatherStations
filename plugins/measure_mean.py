import os
import json
import statistics
from datetime import datetime

with open('C:\\Users\\marek\\Desktop\\WeatherStationsTest\\dags\\data\\weather_data.json', 'r') as file:
    data = json.load(file)
    main = (data['main'])
    pressure = (main['pressure'])
    print(f'Pressure is: {pressure}')
    pressure_data = [1000, 1001, 1002]
    pressure_data.append(pressure)
    print(pressure_data)
    mean_pressure = statistics.mean(pressure_data)
    print(mean_pressure)
    file.close()

# with open('C:\\Users\\marek\\Desktop\\WeatherStationsTest\\dags\\data\\pressure_data.txt', 'a') as file2:
#     data_list = [1000, 1003, 1000]
#     data_list.append(pressure)
#     json.dump(data_list, file2)
#     file2.close()

# with open('C:\\Users\\marek\\Desktop\\WeatherStationsTest\\dags\\data\\pressure_data.txt', 'r') as file3:
#     print(file3)
#     x = statistics.mean(data)