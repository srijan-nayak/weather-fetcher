import requests


def get_valid_city() -> str:
    city = input("Enter city name: ")
    search_response = requests.get(
        f"https://www.metaweather.com/api/location/search/?query={city}")
    if search_response.text == "[]":
        print("City not found!")
        city = get_valid_city()
    return city


try:
    city = get_valid_city()
    search_response = requests.get(
        f"https://www.metaweather.com/api/location/search/?query={city}")
    location_data = search_response.json()
    woeid = location_data[0]["woeid"]
except requests.exceptions.ConnectionError:
    print("Could not connect to the metaweather server!")
