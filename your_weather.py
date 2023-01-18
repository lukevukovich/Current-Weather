import requests
import weather_root

# your_weather.py utilizes two separate APIs to retrieve your location and display the current weather


# Return float values of lat and long response
def get_lat_long_location_api(response):
    return response['latitude'], response['longitude']


def wait():
    try:
        input("\nPress enter to exit...")
    except SyntaxError:
        pass


def main():

    print("your_weather.py\n")

    # Request to get location
    location_url_final = weather_root.LOCATION_URL + weather_root.LOCATION_API_KEY
    location_response = requests.get(location_url_final).json()

    # If location was found
    if len(location_response) > 0:
        
        # Build a string with location credentials
        # Retrieve location via API request
        location_string = ""

        country = location_response['country_code']

        city = location_response['city']
        location_string += city

        # Add state to string if in US
        if country == "US":
            state = location_response['region_iso_code']
            location_string += ", " + state

        location_string += ", " + country

        # Get lat and long of your location
        lat, long = get_lat_long_location_api(location_response)

        # Request for weather
        weather_url = "https://api.openweathermap.org/data/2.5/weather?lat="
        weather_url += str(lat) + "&lon=" + str(long) + "&appid=" + weather_root.WEATHER_API_KEY + "&units=imperial"
        weather_response = requests.get(weather_url).json()

        # If weather was found
        if len(weather_response) > 0:

            # Get weather stats
            temp, maximum, minimum, weather, humidity = weather_root.get_weather_stats(weather_response)

            # Format weather stats
            temp = weather_root.format_stat(temp, 2)
            maximum = weather_root.format_stat(maximum, 2)
            minimum = weather_root.format_stat(minimum, 2)
            humidity = weather_root.format_stat(humidity, 0)

            # Print weather results
            weather_root.print_weather_results(location_string, temp, maximum, minimum, weather, humidity)
            
        else:
            # If weather request has no body content
            print("\nLocation not found")
            
    else:
        # If location request has no body content
        print("\nLocation not found")

    wait()
    exit(0)


main()
