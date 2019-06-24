import requests

while True:
    city = input("Enter city name: ")
    try:
        search_response = requests.get(
            f"https://www.metaweather.com/api/location/search/?query={city}")
        if search_response.text == "[]":
            print("City not found!")
            continue
        location_data = search_response.json()
        woeid = location_data[0]["woeid"]
    except requests.exceptions.ConnectionError:
        print("Could not connect to the metaweather server!")
