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
        points = []
        for j in range(i * 1000 + n * 100, i * 1000 + n * 100 + 100):
            if j >= df.shape[0]:
                break
            points.append((df.iloc[j].Start_Lat, df.iloc[j].Start_Lng, df.iloc[j].Severity))
        if len(points) == 0:
            break

        path = '%7C'.join([f"{points[i][0]}%2C{points[i][1]}" for i in range(len(points))])
        url = f"https://roads.googleapis.com/v1/nearestRoads?points={path}&key={api_key}"
        headers = {'Accept': 'application/json'}

        response = requests.get(url=url, headers=headers)
        places = response.json()['snappedPoints']
        if len(places) < len(points):
            continue
        originalIndices = set()
        for k in range(len(places)):
            if places[k]['originalIndex'] in originalIndices:
                continue
            else:
                originalIndices.add(places[k]['originalIndex'])
            if places[k]['placeId'] in export_dict:
                export_dict[places[k]['placeId']] += [(points[places[k]['originalIndex']][2] ** 0.5, points[places[k]['originalIndex']][0], points[places[k]['originalIndex']][1])]
            else:
                export_dict[places[k]['placeId']] = [(points[places[k]['originalIndex']][2] ** 0.5, points[places[k]['originalIndex']][0], points[places[k]['originalIndex']][1])]

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
        total_severity = sum([i[0] for i in batch[place]])
        if place in export_batches:
            export_batches[place] = (export_batches[place][0] + total_severity, batch[place][0][1], batch[place][0][2])
        else:
            export_batches[place] = (total_severity, batch[place][0][1], batch[place][0][2])

with open("test_road_segs.json", "w") as f:
    f.write(json.dumps(export_batches))