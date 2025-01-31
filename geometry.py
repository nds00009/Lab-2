## Geometry Formula

import math

x1 = int(input("please input a value for x1: "))
y1 = int(input("please input a value for y1: "))
x2 = int(input("please input a value for x2: "))
y2 = int(input("please input a value for y2: "))

m = (y2 - y1)/(x2 - x1)

d = math.sqrt((x2 - x1)**2+(y2 - y1)**2)

print(f"The slope given the points ({x1},{y1}) and ({x2},{y2}) is: {round(m,2)} with a distance apart of {round(d,2)}")
