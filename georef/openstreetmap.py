import requests

def get_lat_lng(address):
    url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json"
    response = requests.get(url)
    data = response.json()
    lat = data[0]["lat"]
    lng = data[0]["lon"]

    return lat, lng

if __name__ == "__main__":
    address = "Av. Insurgentes Sur 1279, Del Valle, 03100 Ciudad de México"
    lat, lng = get_lat_lng(address)
    print(f'latitude: {lat}, longitude: {lng}')
