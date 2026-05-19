import numpy as np

stars = np.array([
    [5600, 1.0, 8.5],
    [4200, 0.7, 12.3],
    [30000, 18.0, 430.0],
    [7800, 1.5, 25.0],
    [3500, 0.3, 4.2]
])

print(stars)

#Here we have created a 2D array where each row represents a star and the columns represent different properties of the stars (temperature, masses and distances).

print(stars.dtype)  # This will print the data type of the elements in the array.
print(stars.shape)  # This will print the dimensions of the array.

#Accessing elements in a 2D array

print(stars[0])         # This will print the first row of the array, which corresponds to the first star.

print(stars[2,0])       # This will print the 1st element of the 3rd row.

print(stars[:, 0])      # This will print the first column of the array, which corresponds to the temperatures of all the stars.

#The ":" means we want all the rows, and "0" means we want the first column

temperatures = stars[:, 0]              #Making temperature array for boolean filtering
hot_stars = stars[temperatures > 6000]  #Creating and applying a boolean mask
print(hot_stars)                        

#Temperatures is a 1D array that contains the first column of the stars array.
#We can use this temperatures array to create a boolean mask and then apply that mask to the stars array to get the rows of the hot stars.
#We can filter 10000 stars with 20 properties by 1 property and get aa separate array of the filtered stars in 2 lines.

print(stars[:, 1])
print(stars[:, 1].mean())

#The first line prints the masses of all the stars and the second line directly prints the mean of the masses.

distances = stars[:, 2]
nearby_stars = stars[distances < 20]
print(nearby_stars)

#Now, we are filtering the stars on the basis of distance and only printing the stars that are closer than 20 light years

