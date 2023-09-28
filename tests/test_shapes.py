import math

import pytest

from geometry_lib import circle, triangle


class TestCircle:
    @classmethod
    def setup_class(cls):
        cls.tested_circle = circle.Circle(10)

    def test_negative_or_zero_radius(self):
        with pytest.raises(ValueError) as e:
            _ = circle.Circle(-10)
        assert "Radius must be a positive number." in str(e.value)

        with pytest.raises(ValueError) as e:
            _ = circle.Circle(0)
        assert "Radius must be a positive number." in str(e.value)

    def test_str_instead_of_radius(self):
        with pytest.raises(ValueError) as e:
            _ = circle.Circle("10")
        assert "Radius must be only of type int or float." in str(e.value)

    def test_area(self):
        assert self.tested_circle.area == math.pi * 10**2


class TestTriangle:
    @classmethod
    def setup_class(cls):
        cls.tested_triangle = triangle.Triangle(10, 20, 25)
        cls.tested_right_triangle = triangle.Triangle(3, 4, 5)

    def test_str_instead_of_sides(self):
        with pytest.raises(ValueError) as e:
            _ = triangle.Triangle("1", "2", "3")
        assert "Sides must be only of type int or float." in str(e.value)

    def test_wrong_number_of_sides(self):
        with pytest.raises(ValueError) as e:
            _ = triangle.Triangle()
        assert "Triangle must have 3 sides." in str(e.value)

        with pytest.raises(ValueError) as e:
            _ = triangle.Triangle(1, 2, 3, 4)
        assert "Triangle must have 3 sides." in str(e.value)

        with pytest.raises(ValueError) as e:
            _ = triangle.Triangle(1, 2)
        assert "Triangle must have 3 sides." in str(e.value)

    def test_negative_or_zero_values_as_sides(self):
        with pytest.raises(ValueError) as e:
            _ = triangle.Triangle(-1, -1, -0.5)
        assert "Sides must be positive numbers." in str(e.value)

        with pytest.raises(ValueError) as e:
            _ = triangle.Triangle(0, 0, 0)
        assert "Sides must be positive numbers." in str(e.value)

    def test_two_sides_greater_than_third(self):
        with pytest.raises(ValueError) as e:
            _ = triangle.Triangle(1, 2, 15)
        assert "Sum of two sides of a triangle must be greater than third side." in str(
            e.value
        )

    def test_is_right_triangle(self):
        assert self.tested_triangle.is_right_triangle == False
        assert self.tested_right_triangle.is_right_triangle == True

    def test_perimeter(self):
        assert self.tested_triangle.perimeter == 10 + 20 + 25
        assert self.tested_right_triangle.perimeter == 3 + 4 + 5

    def test_area(self):
        semi_perimeter = (10 + 20 + 25) / 2
        assert self.tested_triangle.area == math.sqrt(
            semi_perimeter
            * (semi_perimeter - 10)
            * (semi_perimeter - 20)
            * (semi_perimeter - 25)
        )

        assert self.tested_right_triangle.area == (3 * 4) / 2
