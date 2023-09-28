import math

from .shapes import PolygonShape


class Triangle(PolygonShape):
    def __init__(self, *sides: list):
        if not all(isinstance(side, (int, float)) for side in sides):
            raise ValueError("Sides must be only of type int or float.")
        if len(sides) != 3:
            raise ValueError("Triangle must have 3 sides.")
        if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
            raise ValueError("Sides must be positive numbers.")
        if (
            sides[0] >= sides[1] + sides[2]
            or sides[1] >= sides[0] + sides[2]
            or sides[2] >= sides[0] + sides[1]
        ):
            raise ValueError(
                "Sum of two sides of a triangle must be greater than third side."
            )
        super().__init__(*sides)

    @property
    def two_smaller_sides(self):
        if self.max_side:
            return [side for side in self.all_sides if side != self.max_side]

    @property
    def is_right_triangle(self):
        if self.max_side:
            return self.max_side**2 == sum(
                side**2 for side in self.two_smaller_sides
            )
        else:
            return False

    @property
    def area(self):
        if self.is_right_triangle:
            return math.prod(self.two_smaller_sides) / 2
        return math.sqrt(
            self.semiperimeter
            * (self.semiperimeter - self.all_sides[0])
            * (self.semiperimeter - self.all_sides[1])
            * (self.semiperimeter - self.all_sides[2])
        )
