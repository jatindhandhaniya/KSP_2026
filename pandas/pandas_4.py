import pandas as pd

stars = pd.DataFrame({
    "name":        ["Sun-like", "Orange Dwarf", "Blue Giant", "White Star", "Red Dwarf"],
    "temperature": [5600, 4200, 30000, 7800, 3500],
    "mass":        [1.0, 0.7, 18.0, 1.5, 0.3],
    "distance":    [8.5, 12.3, 430.0, 25.0, 4.2],
    "type":        ["K-type", "K-type", "A-type", "A-type", "K-type"]
})

print(stars)

#GROUPBY
#A method used to group different objects together according to one common column.

print(stars.groupby("type")["temperature"].mean())
#type
#A-type    18900.000000
#K-type     4433.333333
#Name: temperature, dtype: float64

#This groups all of the above data according to the groups and since then we can find the temperature values' mean.

print(stars.groupby("type")[["temperature", "mass"]].mean())
#Here, we can find means of temperature and mass together through this syntax.

#APPLYING FUNCTIONS

def kelvin_to_celsius(input):
    return input - 273.15

stars["temp_celsius"] = stars["temperature"].apply(kelvin_to_celsius)
#This will make a new column named Kelvin to Celsius using the above function

print(stars[["name", "temperature", "temp_celsius"]])

#SAVING TO CSV

stars.to_csv("stars_output.csv", index=False)
#This is how we can create a whole new csv file with our processed output