import unittest
from triangle import *

class TriangleTestCase(unittest.TestCase):
    def test_area_correct_integer_input(self):
        res = area(81, 5)
        self.assertEqual(res, 202.5)

    def test_area_correct_float_input(self):
        res = area(5.123123, 20421412.12321124)
        self.assertEqual(res, 52310703.07045116)

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
        res = perimeter(81, 5, 123123)
        self.assertEqual(res, 123209)

    def test_perimeter_correct_float_input(self):
        res = perimeter(101.23432, 24124.13199999, 213)
        self.assertEqual(res, 24438.36631999)

    def test_perimeter_invalid_type_input_1(self):
        res = perimeter("1", 5, "a")
        self.assertEqual(res, "Invalid parameters.")

    def test_perimeter_invalid_type_input_2(self):
        res = perimeter("a", "2", 10312.1111)
        self.assertEqual(res, "Invalid parameters.")

    def test_perimeter_invalid_type_input_3(self):
        res = perimeter([1, 2, 3], 2.3, '2')
        self.assertEqual(res, "Invalid parameters.")

    def test_perimeter_invalid_negative_input(self):
        res = perimeter(-2, -123, 10)
        self.assertEqual(res, "Invalid parameters.")