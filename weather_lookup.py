import requests
import weather_root

# weather_lookup.py utilizes two separate APIs to look up a specific location and display the current weather


def get_lat_long_geo_api(response):
    return response[0]['lat'], response[0]['lon']


def exit_logic(c):
    if c == 'x' or c == 'X':
        return True
    else:
        return False


def main():

    print("weather_lookup.py\n")

    # Get city input from user
    city = input("Enter City (x to quit): ")
    # Check for exit
    exit_program = exit_logic(city)

    while not exit_program:

        # Build string with location credentials
        # Get location input from user
        location_string = ""
        location_string += city

        country = input("Enter Country: ")

        # Get state input if US
        state = ""
        if country == "US":
            state = input("Enter State: ")
            location_string += ", " + state

        location_string += ", " + country

        # Request for location
        geo_url = "http://api.openweathermap.org/geo/1.0/direct?q="
        geo_url += city + "," + state + "," + country + "&limit=5&appid=" + weather_root.WEATHER_API_KEY
        geo_response = requests.get(geo_url).json()

        # If location was found
        if len(geo_response) > 0:

            # Get coordinates of location found
            lat, long = get_lat_long_geo_api(geo_response)

            # Request for weather
            weather_url = "https://api.openweathermap.org/data/2.5/weather?lat="
            weather_url += str(lat) + "&lon=" + str(long) + "&appid=" + weather_root.WEATHER_API_KEY + "&units=imperial"
            weather_response = requests.get(weather_url).json()

            # Get weather stats
            temp, maximum, minimum, weather, humidity = weather_root.get_weather_stats(weather_response)

            # Format weather stats
            temp = weather_root.format_stat(temp, 2)
            maximum = weather_root.format_stat(maximum, 2)
            minimum = weather_root.format_stat(minimum, 2)
            humidity = weather_root.format_stat(humidity, 0)

            # Print weather results
            print()
            weather_root.print_weather_results(location_string, temp, maximum, minimum, weather, humidity)

        else:
            # If geo request has no body content
            print("\nLocation not found")

        # Get state and city input from user
        city = input("\nEnter City (x to quit): ")
        # Check for exit
        exit_program = exit_logic(city)

    exit(0)


main()