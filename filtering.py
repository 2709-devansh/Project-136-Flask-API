import pandas as pd
import csv

rows = []
with open("Stars-Gravity.csv", "r") as f:
    reader = csv.reader(f)
    for a in reader:
        rows.append(a)

headers = rows[0]
headers[0] = "Row Number"
star_data = rows[1:]

distance = []
gravity = []
for b in star_data:
    b[2] = float(b[2])
    b[5] = float(b[5])
    distance.append(b[2])
    gravity.append(b[5])

distance_modified = []
for index, c in enumerate(distance):
    if c <= 100:
        distance_modified.append(star_data[index])

gravity_modified = []
for index, d in enumerate(gravity):
    if d > 150 and d < 350:
        gravity_modified.append(star_data[index])

gravity_distance_merged = []
for e in distance_modified:
    if e in gravity_modified:
        gravity_distance_merged.append(e)

with open("Stars-Filtered.csv", "a+") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(gravity_distance_merged)

print(headers)
print(len(star_data))
print(len(distance_modified))
print(len(gravity_modified))
print(len(gravity_distance_merged))