import requests
import datetime

# GEO URL
# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
# &units=imperial

# CUR WEATHER URL
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

API_KEY = "8870d0224a58f7c518f0892f6d07e6c3"


def exit_logic(c):
    if c == 'x' or c == 'X':
        return True
    else:
        return False


def get_lat_long(response):
    return response[0]['lat'], response[0]['lon']


# Get state and city input from user
country = input("Enter Country (x to quit): ")
# Check for exit
exit_program = exit_logic(country)

while not exit_program:

    state = ""
    if country == 'US':
        state = input("Enter State: ")

    city = input("Enter City: ")

    # Request to get location
    geo_url = "http://api.openweathermap.org/geo/1.0/direct?q="
    geo_url += city + "," + state + "," + country + "&limit=5&appid=" + API_KEY
    geo_response = requests.get(geo_url).json()

    # If location was found
    if len(geo_response) > 0:

        # Get coordinates of location found
        lat, long = get_lat_long(geo_response)
        lat = str(lat)
        long = str(long)

        # Request for weather of coordinates
        weather_url = "https://api.openweathermap.org/data/2.5/weather?lat="
        weather_url += lat + "&lon=" + long + "&appid=" + API_KEY + "&units=imperial"
        weather_response = requests.get(weather_url).json()

        # Get temp value
        temp = weather_response['main']['temp']
        temp = str('{:.2f}'.format(temp))

        high = weather_response['main']['temp_max']
        high = str('{:.2f}'.format(high))

        low = weather_response['main']['temp_min']
        low = str('{:.2f}'.format(low))

        weather = weather_response['weather'][0]['main']

        humidity = weather_response['main']['humidity']
        humidity = str('{:.0f}'.format(humidity))

        r = None
        if state != "":
            r = ("\n" + city + ", " + state + " Results")
        else:
            r = ("\n" + city + ", " + country + " Results")

        date = datetime.datetime.now()
        date = str(date)
        date = date[:-7]
        r += (" (" + date + "):")

        print(r)
        print("Temperature: " + temp + " F")
        print("Max: " + high + " F")
        print("Min: " + low + " F")
        print("Weather: " + weather)
        print("Humidity: " + humidity + "%")

    else:
        # If geo request has no body content
        print("\nLocation not found")

    # Get state and city input from user
    country = input("\nEnter Country (x to quit): ")
    # Check for exit
    exit_program = exit_logic(country)

exit(0)
