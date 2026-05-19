import pandas as pd

stars = pd.DataFrame({
    "name":        ["Sun-like", "Orange Dwarf", "Blue Giant", "White Star", "Red Dwarf"],
    "temperature": [5600, 4200, 30000, 7800, 3500],
    "mass":        [1.0, 0.7, 18.0, 1.5, 0.3],
    "distance":    [8.5, 12.3, 430.0, 25.0, 4.2]
})

print(stars)