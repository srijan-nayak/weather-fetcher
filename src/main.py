import requests


def get_valid_city() -> str:
    city = input("Enter city name: ")
    print("Looking for matching city on the metaweather...")
    request_response = requests.get(
        f"https://www.metaweather.com/api/location/search/?query={city}")
    if request_response.text == "[]":
        print("City not found!")
        city = get_valid_city()
    else:
        print("Done.")
    return city


def get_woeid(city: str) -> str:
    request_response = requests.get(
        f"https://www.metaweather.com/api/location/search/?query={city}")
    location_data = request_response.json()
    woeid = location_data[0]["woeid"]
    return woeid


def get_weather_data(woeid: str) -> dict:
    request_response = requests.get(
        f"https://www.metaweather.com/api/location/{woeid}")
    return request_response.json()


def display_weather_info(weather_data: dict) -> None:
    print("The weather forecast for the next few days:-")
    print("DATE".center(13, " "),
          "STATE".center(13, " "),
          "TEMPERATURE (°C)".center(18, " "),
          "HUMIDITY (%)".center(14, " "),
          sep="|")
    print("=" * 62)
    for forecast in weather_data["consolidated_weather"]:
        state = forecast["weather_state_name"]
        date = forecast["applicable_date"]
        temp = "%.2f" % forecast["the_temp"]
        humidity = str(forecast["humidity"])
        print(date.center(13, " "),
              state.center(13, " "),
              temp.center(18, " "),
              humidity.center(14, " "),
              sep="|")


def fetch_weather() -> None:
    try:
        city = get_valid_city()
        woeid = get_woeid(city)
        weather_data = get_weather_data(woeid)
        display_weather_info(weather_data)
    except requests.ConnectionError:
        print("Could not connect to the server!")
    choice = input("Fetch weather info for another city? [Y/n] ")
    if choice.lower() == "y":
        fetch_weather()


if __name__ == "__main__":
    fetch_weather()
