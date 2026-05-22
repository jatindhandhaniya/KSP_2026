import pandas as pd

stars = pd.DataFrame({
    "name":        ["Sun-like", "Orange Dwarf", "Blue Giant", "White Star", "Red Dwarf"],
    "temperature": [5600, 4200, 30000, 7800, 3500],
    "mass":        [1.0, 0.7, 18.0, 1.5, 0.3],
    "distance":    [8.5, 12.3, 430.0, 25.0, 4.2]
})

print(stars)                    #This prints the whole table like an excel sheet with all the stars in different rows

print(stars["temperature"])     #This prints the temperatures serial wise along with the name and type of the column.

#A single column in a dataframe is called a series.

print(stars["temperature"].mean())  #Mean of the series

hot_stars = stars[stars["temperature"] > 6000]      #Boolean Masking
print(hot_stars)
#Note that it gives the serial numbers as 2 and 3 in the output, that's how pandas keep track of the index from the original dataframe.

print(stars[stars["distance"] < 20])            #Printing and boolena masking together

#DESCRIBE

print(stars.describe())

#        temperature       mass    distance 
#count      5.000000   5.000000    5.000000             This gives the count of each series
#mean   10220.000000   4.300000   96.000000             This gives the mean of each series
#std    11178.640347   7.671049  186.873072             This gives the standard deviation of each series
#min     3500.000000   0.300000    4.200000             This gives the minimum of each series 
#25%     4200.000000   0.700000    8.500000
#50%     5600.000000   1.000000   12.300000             These three are percentiles, like 50% of the values are below this.
#75%     7800.000000   1.500000   25.000000
#max    30000.000000  18.000000  430.000000             This gives the maximum of each series
