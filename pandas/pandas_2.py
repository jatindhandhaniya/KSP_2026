import pandas as pd

stars = pd.read_csv("stars.csv")

print(stars)    #The entire csv is converted to the stars dataframe in one line only.

print(stars.shape)      #Shape of the dataframe (rows, columns)
print(stars.columns)    #This lists down the headings of the columns telling what information is stored in the dataframe.

print(stars.head(3))    #Gives the first 3 rows (0,1,2)

print(stars.tail(3))    #Gives the last 3 rows (7,8,9)

#SORTING

print(stars.sort_values("temperature"))     #Sorted by temperature

print(stars.sort_values("temperature", ascending=False))    #Sorted in decreasing order
