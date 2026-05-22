import pandas as pd

stars = pd.DataFrame({
    "name":        ["Sun-like", "Orange Dwarf", "Blue Giant", "White Star", "Red Dwarf"],
    "temperature": [5600, 4200, 30000, 7800, 3500],
    "mass":        [1.0, 0.7, 18.0, 1.5, 0.3],
    "distance":    [8.5, 12.3, 430.0, 25.0, 4.2]
})

print(stars)

#iloc
#It's use to select a cell, a row or a column by it's index number.

print(stars.iloc[0])    #This prints the whole row 1. along with the headings.

print(stars.iloc[0,2])  #This only prints the value of the 1st row 3rd column.

print(stars.iloc[1:3, 1:3]) #This prints a 2X2 matrix of the values from the 2nd & 3rd row and 2nd & 3rd column.
#Here, everything prints with the serial number so that it's easy to keep track of.

#loc
#It's use to select a cell, a row or a column by name.

print(stars.loc[:, "temperature"])  #Selecting column by the name.  Whole row prints with index.

print(stars.loc[:, ["name", "temperature"]])    #Two columns in square brackets. Prints with index

#In my project, I will use loc more than iloc.

#ADDING & DROPPING COLUMNS

stars["luminosity"] = [0.8, 0.2, 150000.0, 8.0, 0.01]
print(stars)        #Now a 5th column is added to the whole dataframe

stars = stars.drop(columns=["luminosity"])  #This will drop the luminosity column entirely.
print(stars)

#MISSING VALUES

stars["luminosity"] = [0.8, None, 150000.0, None, 0.01]
print(stars)        #None will save as NaN in the dataframe

#We can do 3 things with the missing values

print(stars.isnull())   #This will print the whole dataframe filled with trues and falses. Trues at NaN places.

print(stars.isnull().sum())     #This sums up the number of trues in each colums and prints column wise.
#In a catalogue of 10000 rows, this tells exactly which column has data quality problems.

print(stars.dropna())   #This prints only the rows after dropping the rows containing even a single NaN

print(stars.fillna(0))  #This fills all the NaN positions with the number in the bracket.

mean_luminosity = stars["luminosity"].mean()
print(stars.fillna(mean_luminosity))        #This fill the NaN positions with the mean luminosity.

#MERGING

radio_data = pd.DataFrame({
    "name":       ["Sun-like", "Blue Giant", "Red Dwarf"],
    "radio_flux": [0.002, 1.45, 0.001]
})

print(pd.merge(stars, radio_data, on="name"))       #on="name" means the merging will be done according to the name column
#This gives an inner join with only the matching names as output.

print(pd.merge(stars, radio_data, on="name", how="left"))   #Here, we added how="left" which means that left column will remain intact.
#All the other columns will be filled by NaN if data is not available during merging.