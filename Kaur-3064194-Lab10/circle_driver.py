'''
Author: Manvir Kaur
KUID: 3064194
Date: 11/15/2021
Lab: lab10
Last modified: 11/15/2021
Purpose: Creating Circles
'''

from circle import Circle

def user_circle():
    print("Enter informaiton for Circle:")
    r = int(input("Radius: "))
    x = int(input("X Position: "))
    y = int(input("Y Position: "))
    return Circle(r, x, y)

def print_circle_info(circ, name = "Circle"):
    print()
    print("Information for " + name)
    print("location: (" + str(circ.xPos) + ", " + str(circ.yPos) + ")")
    print("diameter: " + str(circ.diameter()))
    print("area: " + str(circ.area()))
    print("circumference: " + str(circ.circumference()))
    print("distance from the origin: " + str(circ.dist_to_origin()))

def main():
    circ1 = user_circle()
    circ2 = user_circle()
    print_circle_info(circ1, "Circle 1")
    print_circle_info(circ2, "Circle 2")
    print(circ1.intersect(circ2))

main()
