import unittest
import triangle

class TestTriangleCase(unittest.TestCase):
    def test_positive_perimeter(self):
        result = triangle.perimeter(5, 5, 2)
        self.assertEqual(result, 12)

    def test_zero_perimetr(self):
        result = triangle.perimeter(2, 5, 0)  # Side can not be 0
        self.assertEqual(result, 0)

    def test_positive_area(self):
        result = triangle.area(5, 2)
        self.assertEqual(result, 5)

    def test_zero_area(self):
        result = triangle.area(2, 0)  # Side can not be 0
        self.assertEqual(result, 0)



