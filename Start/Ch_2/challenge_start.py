# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import defaultdict

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

summary = defaultdict(int)
for feature in data["features"]:
    summary[feature["properties"]["type"]] += 1

#print(summary)
for key, value in summary.items():
    print(key, ":", value)
