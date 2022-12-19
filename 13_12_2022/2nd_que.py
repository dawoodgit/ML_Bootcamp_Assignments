#WAP to accept radius of a Circle from the user and calculate area and circumference
from math import pi
radius = int(input("Please provide the radius of the circle:"))

area = pi*(radius**2)
circum = 2*pi*radius

print("The area of this circle is {area} & the cicrcumference is {circum}".format(area = area , circum = circum))