import math

from .shapes import PlaneShape


class Circle(PlaneShape):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise ValueError("Radius must be only of type int or float.")
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2
