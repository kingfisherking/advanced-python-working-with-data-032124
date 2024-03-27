# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime


# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD
def getsig(dataitem): #function for getting significance
    sig = dataitem["properties"]["sig"]
    if (sig is None):
        sig = 0
    return int(sig)
data["features"].sort(key=getsig, reverse=True) #sort data
newdata = data["features"][:40] #first 40 items = top 40
newdata.sort(key=lambda q: q["properties"]["time"], reverse=True) #sort again
header = ["Magnitude", "Place", "Felt Reports", "Date", "Link"]
rows = []

for quake in newdata:
    date = datetime.date.fromtimestamp(
        int(quake["properties"]["time"]/1000))
    latitude = quake["geometry"]["coordinates"][1]
    longitude = quake["geometry"]["coordinates"][0]
    felt = quake["properties"]["felt"]
    if felt is None:
        felt = 0
    map = f"https://maps.google.com/maps/search/?api=1&query={latitude}%2C{longitude}"
    rows.append([
        quake["properties"]["mag"],
        quake["properties"]["place"],
        felt,
        date,
        map
    ])

with open("challengequakes.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)