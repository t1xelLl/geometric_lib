import unittest
import circle


class CircleTestCase(unittest.TestCase):
    def test_negative_perimetr(self):
        result = circle.perimeter(-2)
        self.assertEqual(result, "Error")  # "The radius cannot be negative"

    def test_positive_perimeter(self):
        result = circle.perimeter(5)
        self.assertAlmostEqual(result, 31.4)

    def test_zero_perimeter(self):
        result = circle.perimeter(0)  # Side can not be 0
        self.assertEqual(result, 0)

    def test_negative_area(self):
        result = circle.perimeter(-2)
        self.assertEqual(result, "Error")  # "The radius cannot be negative"

    def test_positive_area(self):
        result = circle.area(5)
        self.assertAlmostEqual(result, 78.53981633974483)

    def test_zero_area(self):
        result = circle.area(0)  # Side can not be 0
        self.assertEqual(result, 0)






