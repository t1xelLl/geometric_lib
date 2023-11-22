import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_perimeter(self):
        result = rectangle.perimeter(0, 1)  # Side can not be 0
        self.assertEqual(result, 0)

    def test_square_perimeter(self):
        result = rectangle.perimeter(5, 5)
        self.assertEqual(result, 20)

    def test_zero_area(self):
        result = rectangle.area(10, 0)  # Side can not be 0
        self.assertEqual(result, 0)

    def test_square_area(self):
        result = rectangle.area(5, 5)
        self.assertEqual(result, 25)



