import csv
import math
import json

data = []
with open("backend/test_road_segs.json", "r") as f:
    data = json.loads(f.read())
    
sum_severity = 0

num_of_roadsegs = len(data)
for road_seg in data:
    sum_severity += int(data[road_seg])
mean = sum_severity/num_of_roadsegs

print("sum of total severity:" + str(sum_severity))
print("number of severity values:" + str(num_of_roadsegs))
print("Mean:" + str(mean))

sigma = 0

for road_seg in data:
    sigma += (data[road_seg] - mean)**2

stdev = math.sqrt(sigma/num_of_roadsegs)
print("Stdev:" + str(stdev))



    