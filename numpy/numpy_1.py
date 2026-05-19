import numpy as np

temperatures = np.array([5600, 4200, 30000, 7800, 3500]) #We are passing a list of temperatures to the np.array() function to create a NumPy array. 

print(temperatures)
print(temperatures + 1000)

#Here we can see that we can print the whole list and add 1,000 to each of the numbers by just one command.
#This is called vectorization. It performs the same operation to all of the things rather than going one by one.

#But in normal Python, we will have to make a loop to add 1,000 to print each of the numbers.
temperatures_normal = [5600, 4200, 30000, 7800, 3500]

for temp in temperatures_normal:
    print(temp + 1000)
    

#Methods in NumPy

print(temperatures.mean())
print(temperatures.max())
print(temperatures.min())

#No loop, no tension. NumPy does all of the calculations internally.

##Boolean Filtering
hot_stars = temperatures[temperatures > 6000]
print(temperatures>6000)       #This is called a boolean mask. This will print a list of True and False values with True for the values that are greater than 6000.
print(hot_stars)               #This will print the values that are greater than 6000. This is called boolean filtering.

#Understanding how masking works

star_names = np.array(["Sun-like", "Orange Dwarf", "Blue Giant", "White Star", "Red Dwarf"])

hot_star_names = star_names[temperatures > 6000]
print(hot_star_names)

#Here, we are using the temperatures array to create a boolean mask and then applying that mask to the star_names array to get the names of the hot stars.
#This is very common in astronomy where we have to filter star names based on their temperatures or other properties.

print(temperatures.shape) #This is the Numpy's way of saying the number of elements the dimension. It's one dimension, so it will print (5,). If it were a 2D array, it would print something like (5, 3) for 5 rows and 3 columns.
print(temperatures.dtype) #This will print the data type of the elements in the array. In this case, it will be int64 because the temperatures are integers.

