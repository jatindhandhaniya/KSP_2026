import numpy as np

import numpy as np

# 10 stars — columns: Temperature (K), Mass (solar), Distance (ly), Brightness (magnitude)
catalogue = np.array([
    [5600,  1.0,   8.5,   4.8],
    [4200,  0.7,  12.3,   6.1],
    [30000, 18.0, 430.0,  2.1],
    [7800,  1.5,  25.0,   3.9],
    [3500,  0.3,   4.2,   8.3],
    [9500,  2.1,  18.0,   3.1],
    [6200,  1.1,   9.7,   4.2],
    [3800,  0.4,   6.5,   7.9],
    [12000, 3.5,  55.0,   2.8],
    [4800,  0.9,  14.0,   5.5]
])

print(catalogue.shape)  #This will print the dimensions of the catalogue array, which is (10, 4)

temperatures = catalogue[:, 0]  #1st column of the catalogue
masses       = catalogue[:, 1]  #2nd column of the catalogue
distances    = catalogue[:, 2]  #3rd column of the catalogue
brightness   = catalogue[:, 3]  #4th column of the catalogue

print(temperatures) #This will print the temperatures of all the stars in the catalogue.

print(temperatures.mean())
#This will print the mean temperature of the stars.

print(distances.mean())
#This will print the mean distances of the stars.

lessThan20Distance = catalogue[distances<20]
print(lessThan20Distance)
#Self-explanotry

hotterAndCloser = catalogue[(distances<50) & (temperatures>6000)]
print(hotterAndCloser)
#Self-explanotry

brightestStar = brightness.min()
print(catalogue[brightness == brightestStar])
#In astro, the brightest star has the least magnitude of the brightness magnitude

#In Numpy, there is a limitation of labels.
#In real catalogues, we have names attached with the labels but currently we have no way for that.
#That's why Pandas is used.
