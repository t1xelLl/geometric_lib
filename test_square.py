import unittest
import square

class SquareTestCase(unittest.TestCase):
    def test_zero_perimeter(self):
        result = square.perimeter(0)  # Side can not be 0
        self.assertEqual(result, 0)

    def test_negative_perimetr(self):
        with self.assertRaises(ValueError):
            result = square.perimeter(-1)

    def test_positive_perimeter(self):
        result = square.perimeter(5)
        self.assertEqual(result, 20)

    def test_zero_area(self):
        result = square.area(0)  # Side can not be 0
        self.assertEqual(result, 0)

    def test_positive_area(self):
        result = square.area(5)
        self.assertEqual(result, 25)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            result = square.area(-1)

