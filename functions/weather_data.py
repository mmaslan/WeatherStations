import datetime
import pyowm


api_key = "588237482f885cef420a4fa9796cd1b9"
owm = pyowm.OWM(api_key).weather_manager()


def print_weather(data):
    ref_time = datetime.datetime.fromtimestamp(data.ref_time).strftime('%Y-%m-%d %H:%M')
    print(f"Time\t\t: {ref_time}")
    print(f"Overview\t: {data.detailed_status}")
    print(f"Wind Speed\t: {data.wind()}")
    print(f"Humidity\t: {data.humidity}")
    print(f"Temperature\t: {data.temperature('celsius')}")
    print(f"Rain\t\t: {data.rain.get('ilość_opadów', 0)}") # .get(key, value) -> ValueError?
    print("\n")


def get_current_weather(city):
    weather_api = owm.weather_at_place(city)  # give where you need to see the weather
    weather_data = weather_api.weather  # get out data in the mentioned location

    print(f"Current Weather at {city}")
    print_weather(weather_data)
    print("\n")


if __name__ == '__main__':
    get_current_weather('Warsaw')
    get_current_weather('Gdansk')
