import json
import pandas
import requests
import overpy
import geopy.distance
from threading import Thread, Lock
from time import sleep

api_key = 'AIzaSyBgKOoB2j5OFR2CmvmYLlT2Llobhr42ojk'

data = {}
new_data = {}
with open("backend/test_road_segs.json", "r") as f:
    data = json.loads(f.read())
data_segs = [i for i in data]

lock = Lock()

def process_places(i: int):
    seg = (len(data_segs) // 600)
    for j in range(i * seg, i * seg + seg):
        if j >= len(data_segs):
            break
        road_seg = data_segs[j]
        print(road_seg)
        headers = {'Accept': 'application/json', 'X-Goog-Api-Key': api_key}
        # breakpoint()
        print(response.json())
        location = response.json()['location']
        lat, lng = location['latitude'], location['longitude']

        url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={api_key}"

        response = requests.get(url=url, headers=headers)

        # address_components = response.json()['results'][0]['address_components']
        # state = ""
        # for component in address_components:
        #     if component['types'][0] == 'administrative_area_level_1':
        #         state = component['short_name']

        viewport = response.json()['results'][0]['geometry']['viewport']
        size = geopy.distance.geodesic((viewport['northeast']['lat'], viewport['northeast']['lng']), (viewport['southwest']['lat'], viewport['southwest']['lng'])).mi
        
        # api = overpy.Overpass()
        # result = api.query(f"""way(around:{500},{lat},{lng}) ["maxspeed"];(._;>;);out body;""")
        # sum_speed_limit = 0
        # for way in result.ways:
        #     sum_speed_limit += int(way.tags.get("maxspeed", "n/a").split()[0])
        # if not len(result.ways):
        #     continue
        # avg_speed_limit = sum_speed_limit / len(result.ways)
        
        lock.acquire()
        new_data[road_seg] = data[road_seg] / size
        lock.release()
        sleep(1.2)
    
    print(i)
    
threads = []
for i in range(600):
    thread = Thread(target=process_places, args=[i])
    thread.start()

for thread in threads:
    thread.join()

with open("test_road_segs1.json", "w") as f:
    f.write(json.dumps(new_data))