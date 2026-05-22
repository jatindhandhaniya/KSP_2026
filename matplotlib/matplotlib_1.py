import matplotlib.pyplot as plt
import numpy as np

temperatures = np.array([5600, 4200, 30000, 7800, 3500, 9500, 6200, 3800, 12000, 4800])
brightness   = np.array([4.8, 6.1, 2.1, 3.9, 8.3, 3.1, 4.2, 7.9, 2.8, 5.5])

plt.scatter(temperatures, brightness)   #This tells to make a scatter plot b/w temperatures and brightness

plt.xlabel("Temperature (K)")           #X label
plt.ylabel("Brightness (Magnitude)")    #Y label
plt.title("Temperature vs Brightness")  #Title

plt.gca().invert_yaxis()                #Invert the y-axis upside down

plt.scatter(temperatures, brightness, c=temperatures, cmap="hot")   
#In this scatter plot, there is a color bar which determines the colours of the points, hot is a gradient of a big gradient library.
plt.colorbar(label="Temperature (K)")       

hot_temps = temperatures[temperatures > 6000]       #Using numpy arrays
cool_temps = temperatures[temperatures <= 6000]

hot_brightness = brightness[temperatures > 6000]
cool_brightness = brightness[temperatures <= 6000]

plt.scatter(hot_temps, hot_brightness, c="red", label="Hot stars")  
plt.scatter(cool_temps, cool_brightness, c="blue", label="Cool stars")
plt.legend()
plt.gca().invert_yaxis()
plt.xlabel("Temperature (K)")
plt.ylabel("Brightness (Magnitude)")    
plt.title("Hot vs Cool Stars")

plt.savefig("hot_vs_cool.png", dpi=150, bbox_inches="tight")    #To save the figure

plt.show()