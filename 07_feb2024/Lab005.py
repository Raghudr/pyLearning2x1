# Task #1
# Write a Python program to calculate the area of a circle given its radius
# using the formula area=π×r^2 ( Take pie as 3.14)

r = float(input("Input the radius of the circle : "))
pi=3.14
area = pi * r ** 2
print("The area of the circle with radius " + str(r) + " is: " + str(area))
