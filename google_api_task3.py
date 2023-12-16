import googlemaps
from datetime import datetime

def get_geocoding_info(api_key, address):
    # Initialize the Google Maps client
    gmaps = googlemaps.Client(key=api_key)

    try:
        # Geocode the given address
        geocode_result = gmaps.geocode(address)

        if geocode_result:
            # Extract relevant information
            location = geocode_result[0]['geometry']['location']
            formatted_address = geocode_result[0]['formatted_address']

            print(f"Address: {formatted_address}")
            print(f"Latitude: {location['lat']}, Longitude: {location['lng']}")
        else:
            print(f"No results found for the address: {address}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Replace 'YOUR_API_KEY' with your actual Google Maps API key
api_key = 'YOUR_API_KEY'

# Replace '1600 Amphitheatre Parkway, Mountain View, CA' with the address you want to geocode
address_to_geocode = '1600 Amphitheatre Parkway, Mountain View, CA'

# Fetch and display geocoding information
get_geocoding_info(api_key, address_to_geocode)
