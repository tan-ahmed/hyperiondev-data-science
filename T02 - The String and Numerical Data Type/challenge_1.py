import math

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

s = (side1 + side2 + side3) / 2

area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

print("The area of the triangle is:", area)
