import numpy as np

temperatures = np.array([5600, 4200, 30000, 7800, 3500, 9500, 6200, 3800, 12000, 4800])

#np.where
#This tells about the position in the array where a certain condition matches.

print(np.where(temperatures > 6000))

star_names = np.array(["Sun-like", "Orange Dwarf", "Blue Giant", "Sirius-like", "Red Dwarf",
                        "White Star", "Yellow Star", "Red Dwarf 2", "Hot Giant", "Cool Dwarf"])

hot_indices = np.where(temperatures > 6000)     #Here, we are naming the indices positions as the hot_indices and we can use them in multiple place without re declaring the condition multiple times.
print(star_names[hot_indices])

print(star_names[temperatures>6000])        #This also does the same thing but the above method is cleaner and more reusable.

#np.concatenate
#This joins two arrays

catalogue_1 = np.array([1,2,3,4])
catalogue_2 = np.array([5,6,7,8,9])

combined = np.concatenate([catalogue_1, catalogue_2])
print(combined)                      #[1 2 3 4 5 6 7 8 9]

#Very simple concatenation process.

#np.zeros
#This makes an array of certain length with 0s in it which can later be replaced.

empty_catalogue = np.zeros(5)
print(empty_catalogue)              #[0. 0. 0. 0. 0.]

empty_catalogue[2] = 99

print(empty_catalogue)              #[ 0.  0. 99.  0.  0.]

#Similarly, an np.ones also exists, does the same work. No difference. 

