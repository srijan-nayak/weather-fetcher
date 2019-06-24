import requests


def get_valid_city() -> str:
    city = input("Enter city name: ")
    search_response = requests.get(
        f"https://www.metaweather.com/api/location/search/?query={city}")
    if search_response.text == "[]":
        print("City not found!")
        city = get_valid_city()
    return city


def get_woeid(city: str) -> str:
    search_response = requests.get(
        f"https://www.metaweather.com/api/location/search/?query={city}")
    location_data = search_response.json()
    woeid = location_data[0]["woeid"]
    return woeid


def get_weather_data(woeid: str) -> dict:
    request_response = requests.get(
        f"https://www.metaweather.com/api/location/{woeid}")
    return request_response.json()


try:
    city = get_valid_city()
    woeid = get_woeid(city)
    weather_data = get_weather_data(woeid)
except requests.ConnectionError:
    print("Could not connect to the server!")
