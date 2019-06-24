import requests

while True:
    city = input("Enter city name: ")
    try:
        search_response = requests.get(
            f"https://www.metaweather.com/api/location/search/?query={city}")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the metaweather server!")
