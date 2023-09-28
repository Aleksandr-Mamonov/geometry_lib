class Shape:
    pass


class PlaneShape(Shape):
    pass


class SolidShape(Shape):
    pass


class PolygonShape(PlaneShape):
    def __init__(self, *sides):
        self._sides_lengths = [side for side in sides]

    @property
    def all_sides(self):
        return self._sides_lengths

    @property
    def perimeter(self):
        return sum(self.all_sides)

    @property
    def semiperimeter(self):
        return self.perimeter / 2

    @property
    def max_side(self):
        biggest_side = max(self.all_sides)
        return biggest_side if self.all_sides.count(biggest_side) == 1 else None
