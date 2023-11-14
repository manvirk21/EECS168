'''
Author: Manvir Kaur
KUID: 3064194
Date: 11/15/2021
Lab: lab10
Last modified: 11/15/2021
Purpose: Creating Circles
'''

from math import pi

class Circle:
    def __init__(self, radius, xPos, yPos):
        self.radius = radius
        self.xPos = xPos
        self.yPos = yPos

    def diameter(self):
        return self.radius * 2

    def area(self):
        return pi * self.radius**2

    def circumference(self):
        return 2 * pi * self.radius

    def dist_to_origin(self):
        return (self.xPos**2 + self.yPos**2)**1/2

    def intersect(self, other_circle):
        return ((self.xPos - other_circle.xPos)**2 + (self.yPos - other_circle.yPos)**2)**1/2 < self.radius + other_circle.radius
    
