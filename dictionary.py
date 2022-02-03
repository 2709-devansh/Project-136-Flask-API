import csv

rows = []
with open("Stars-Filtered.csv", "r") as f:
    reader = csv.reader(f)
    for i in reader:
        rows.append(i)

headers = rows[0]
star_data = rows[1:]

star_dict = []
for j in star_data:
    temp_dict = {
        "name":j[1],
        "distance":j[2],
        "mass":j[3],
        "radius":j[4],
        "gravity":j[5]
    }
    star_dict.append(temp_dict)

print(star_dict)