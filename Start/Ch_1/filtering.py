# Example file for Advanced Python: Working With Data by Joe Marini
# using the filter() function to filter a data set

import json


def filterEvens(x):
    # filters out even numbers and keeps odd numbers
    if x % 2 == 0:
        return False
    return True


def filterUppers(x):
    # filters out upper-case letters and keeps lower case letters
    if x.isupper():
        return False
    return True


# define some sample sequences to operate on
nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
chars = "abcDeFGHiJklmnoP"

# TODO: use filter to remove items from a list
filteredNum = filter(filterEvens, nums)

# TODO: use filter on non-numeric sequence
filteredChars = filter(filterUppers, chars)
# Use the filter on our data - let's filter out all seismic events that were *not* quakes
# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def notQuake(dataitem):
    if dataitem["properties"]["type"] == "earthquake":
        return False
    return True

notQuakes = list(filter(notQuake, data["features"]))

for x in range(5):
    print(notQuakes[x]["properties"]["type"])