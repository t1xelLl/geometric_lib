import unittest
import circle


class CircleTestCase(unittest.TestCase):
    def test_negative_perimetr(self):
        with self.assertRaises(ValueError):
            result = circle.perimeter(-2) # "The radius cannot be negative"


    def test_positive_perimeter(self):

        result = circle.perimeter(5)
        self.assertAlmostEqual(result, 31.4)

    def test_zero_perimeter(self):
        result = circle.perimeter(0)  # Side can not be 0
        self.assertEqual(result, 0)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            result = circle.perimeter(-2)  # "The radius cannot be negative"

    def test_positive_area(self):
        result = circle.area(5)
        self.assertAlmostEqual(result, 78.5)

    def test_zero_area(self):
        result = circle.area(0)  # Side can not be 0
        self.assertEqual(result, 0)






