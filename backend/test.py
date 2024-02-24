import requests
import json
import polyline
from collections import Counter

api_key = 'AIzaSyDt14tmG4wv0zqJ6rTYBlPftB0w4VzwSgY'
url = f"https://routes.googleapis.com/directions/v2:computeRoutes?key={api_key}"
headers = {'Accept': 'application/json', 'X-Goog-FieldMask': 'routes.polyline.encodedPolyline'}

cstat_latlng = {"latitude": 30.627977, "longitude": -96.334404}
dallas_latlng = {"latitude": 32.776665, "longitude": -96.796989}

cstat_location = {"latLng": cstat_latlng, "heading": 0}
dallas_location = {"latLng": dallas_latlng, "heading": 0}

cstat_waypoint = {"via": False, "vehicleStopover": False, "sideOfRoad": False, "location": cstat_location}
dallas_waypoint = {"via": False, "vehicleStopover": False, "sideOfRoad": False, "location": dallas_location}

request = {
    "origin": cstat_waypoint,
    "destination": dallas_waypoint,
    "intermediates": [],
    "travelMode": "DRIVE",
    "computeAlternativeRoutes": True,
}

request = json.dumps(request)

response = requests.post(url=url, data=request, headers=headers)

route = polyline.decode(response.json()['routes'][0]['polyline']['encodedPolyline'])
places = []

for i in range(len(route) // 100):
    path = '%7C'.join([f"{lat}%2C{long}" for lat, long in route[i * 100:i * 100 + 100]])
    url = f"https://roads.googleapis.com/v1/snapToRoads?interpolate=true&path={path}&key={api_key}"
    headers = {'Accept': 'application/json'}

    response = requests.get(url=url, headers=headers)
    for place in response.json()['snappedPoints']:
        places.append(place['placeId'])
    