# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# TODO: The min() function finds the minimum value
# print("The minimum value of values is: ", min(values))
# print("The minimum value of strings is: ", min(strings))

# TODO: The max() function finds the maximum value
# print("The maximum value of values is: ", max(values))
# print("The maximum value of strings is: ", max(strings))

# TODO: define a custom "key" function to extract a data field
# print("The minimum length of strings is: ", min(strings, key=len))
# print("The maximum length of strings is: ", max(strings, key=len))

# TODO: open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile) 

print(len(data["features"]))
def getmag(dataitem):
    magnitude = dataitem["properties"]["mag"]
    if magnitude is None:
        magnitude = 0
    return(float(magnitude))
print("The biggest magnitude was:", max(data["features"], key=getmag))