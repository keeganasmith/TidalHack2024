import pandas as pd
import requests
import json
from threading import Thread, Lock

api_key = 'AIzaSyDt14tmG4wv0zqJ6rTYBlPftB0w4VzwSgY'
df = pd.read_csv("test_accidents.csv")

batches = []
lock = Lock()

def get_points_batch(i: int):
    export_dict = {}
    for n in range(10):
        points = {}
        for j in range(i * 1000 + n * 100, i * 1000 + n * 100 + 100):
            if j >= df.shape[0]:
                break
            if (df.iloc[j].Start_Lat, df.iloc[j].Start_Lng) in points:
                points[(df.iloc[j].Start_Lat, df.iloc[j].Start_Lng)].append(df.iloc[j].Severity)
            else:
                points[(df.iloc[j].Start_Lat, df.iloc[j].Start_Lng)] = [df.iloc[j].Severity]

        if len(points) == 0:
            break

        path = '%7C'.join([f"{lat}%2C{points[i][1]}" for i in range(len(points))])
        url = f"https://roads.googleapis.com/v1/snapToRoads?interpolate=true&path={path}&key={api_key}"
        headers = {'Accept': 'application/json'}

        response = requests.get(url=url, headers=headers)
        places = response.json()['snappedPoints']
        breakpoint()
        for place in places:
            if place['placeId'] in export_dict:
                export_dict[place['placeId']] += sum([i ** 0.5 for i in points[(place['Latitude'], place['Longitude'])]])
            else:
                export_dict[place['placeId']] = sum([i ** 0.5 for i in points[(place['Latitude'], place['Longitude'])]])

    lock.acquire()
    batches.append(export_dict)
    print(i)
    lock.release()

threads = []
for i in range(df.shape[0] // 1000):
    thread = Thread(target=get_points_batch, args=[i])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

export_batches = {}
for batch in batches:
    for place in batch:
        if place in export_batches:
            export_batches[place] += batch[place]
        else:
            export_batches[place] = batch[place]

with open("test_road_segs.json", "w") as f:
    f.write(json.dumps(export_batches))