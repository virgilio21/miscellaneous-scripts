import requests


def get_lat_lng(address, access_token):

    address.replace(" ", "%20")
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json?access_token={access_token}&limit=1"

    return requests.get(url)

    
if __name__ == "__main__":

    address = "1600 Amphitheatre Parkway, Mountain View, CA"
    access_token = "YOUR_ACCESS_TOKEN"

    response = get_lat_lng(address, access_token)
    if response.status_code == 200:
        data = response.json()
        latitude = data["features"][0]["geometry"]["coordinates"][1]
        longitude = data["features"][0]["geometry"]["coordinates"][0]
        print("Latitude:", latitude)
        print("Longitude:", longitude)
    else:
        print("Error:", response.text)