# This is a program that accepts inputs from users and calculates the area of a rectangle

# The following function receives the inputed values for length and breadth and returns the area
def area_of_rectangle(length, breadth):
    result = length * breadth
    return result

# comments
print("This program calculates the area of a rectangle")
length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
area = area_of_rectangle(length, breadth)

print(f"The area of the rectangle is {area}")

