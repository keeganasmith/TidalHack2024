import requests

url = 'https://routes.googleapis.com/directions/v2:computeRoutes'
api_key = 'YOUR_API_KEY'

headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key': api_key,
    'X-Goog-FieldMask': 'routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline'
}

data = {
  "origin":{
    "location":{
      "latLng":{
        "latitude": 37.419734,
        "longitude": -122.0827784
      }
    }
  },
  "destination":{
    "location":{
      "latLng":{
        "latitude": 37.417670,
        "longitude": -122.079595
      }
    }
  },
  "travelMode": "DRIVE",
  "routingPreference": "TRAFFIC_AWARE",
  "departureTime": "2023-10-15T15:01:23.045123456Z",
  "computeAlternativeRoutes": False,
  "routeModifiers": {
    "avoidTolls": False,
    "avoidHighways": False,
    "avoidFerries": False
  },
  "languageCode": "en-US",
  "units": "IMPERIAL"
}

response = requests.post(url, json=data, headers=headers)
print(response.json())