# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json
from minmax import getmag
from transform import simplify



def getsig(quake):
    significance = quake["properties"]["sig"]
    if significance is None:
        significance = 0
    return int(significance)

def getfelt(quake):
    felt = quake["properties"]["felt"]
    if felt is None:
        felt = 0
    return felt

def simplify2(quake):
    simpleJSON = simplify(quake)
    simpleJSON["significance"] = getsig(quake)
    simpleJSON["reports"] = getfelt(quake)
    return simpleJSON


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

print("total number of quakes:",len(data["features"]))
print("# felt by at least 100:", sum(
    quake["properties"]["felt"] is not None
    and quake["properties"]["felt"] >= 100
    for quake in data["features"]
))
print("most felt:",simplify2(max(data["features"], key=getfelt)))
data["features"].sort(key=getsig, reverse=True)
for x in range(10):
    print(x+1,
          simplify2(data["features"][x])["location"],
          simplify2(data["features"][x])["significance"])