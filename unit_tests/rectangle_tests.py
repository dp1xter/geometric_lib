import unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
    def test_area_correct_integer_input(self):
        res = area(81, 5)
        self.assertEqual(res, 405)

    def test_area_correct_float_input(self):
        res = area(5.123123, 20421412.12321124)
        self.assertEqual(res, 104621406.14090233)

    def test_area_invalid_type_input_1(self):
        res = area("1", 5)
        self.assertEqual(res, "Invalid parameters.")

    def test_area_invalid_type_input_2(self):
        res = area("a", "2")
        self.assertEqual(res, "Invalid parameters.")

    def test_area_invalid_type_input_3(self):
        res = area([1, 2, 3], 2.1)
        self.assertEqual(res, "Invalid parameters.")

    def test_area_invalid_negative_input(self):
        res = area(-2, 10)
        self.assertEqual(res, "Invalid parameters.")

    def test_perimeter_correct_integer_input(self):
        res = perimeter(81, 5)
        self.assertEqual(res, 172)

    def test_perimeter_correct_float_input(self):
        res = perimeter(101.23432, 24124.13199999)
        self.assertEqual(res, 48450.73263998)

    def test_perimeter_invalid_type_input_1(self):
        res = perimeter("1", 5)
        self.assertEqual(res, "Invalid parameters.")

    def test_perimeter_invalid_type_input_2(self):
        res = perimeter("a", "2")
        self.assertEqual(res, "Invalid parameters.")

    def test_perimeter_invalid_type_input_3(self):
        res = perimeter([1, 2, 3], 2.3)
        self.assertEqual(res, "Invalid parameters.")

    def test_perimeter_invalid_negative_input(self):
        res = perimeter(-2, -123)
        self.assertEqual(res, "Invalid parameters.")
