# Assignment 2 - Python Programs

# 1. Area of Rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area_rectangle = length * width
print("Area of Rectangle:", area_rectangle)

# 2. Perimeter of Square
side = float(input("\nEnter side of square: "))
perimeter_square = 4 * side
print("Perimeter of Square:", perimeter_square)

# 3. Area of Triangle
base = float(input("\nEnter base of triangle: "))
height = float(input("Enter height of triangle: "))
area_triangle = 0.5 * base * height
print("Area of Triangle:", area_triangle)

# 4. Circumference of Circle
radius = float(input("\nEnter radius of circle: "))
circumference = 2 * 3.14 * radius
print("Circumference of Circle:", circumference)

# 5. Simple Interest
P = float(input("\nEnter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))
SI = (P * R * T) / 100
print("Simple Interest:", SI)
