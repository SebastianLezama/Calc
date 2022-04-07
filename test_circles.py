import unittest
from main import circle_area
from math import pi


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(4.7), pi*4.7**2)

    def test_value_error(self):
        self.assertRaises(ValueError, circle_area, -3)

    def test_types(self):
        self.assertRaises(TypeError, circle_area, 5j+6)
        self.assertRaises(TypeError, circle_area, "ttrr")


if __name__ == "__main__":
    unittest.main()

