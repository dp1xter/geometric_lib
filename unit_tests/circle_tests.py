import unittest
from circle import *

class CircleTestCase(unittest.TestCase):
    def test_area_correct_integer_input(self):
        res = area(81)
        self.assertEqual(res, 20611.98940020263)

    def test_area_correct_float_input(self):
        res = area(101.23432)
        self.assertEqual(res, 32196.259025222444)

    def test_area_invalid_type_input_1(self):
        res = area("1")
        self.assertEqual(res, "Invalid parameters.")

    def test_area_invalid_type_input_2(self):
        res = area("a")
        self.assertEqual(res, "Invalid parameters.")

    def test_area_invalid_type_input_3(self):
        res = area([1, 2, 3])
        self.assertEqual(res, "Invalid parameters.")

    def test_area_invalid_negative_input(self):
        res = area(-2)
        self.assertEqual(res, "Invalid parameters.")

    def test_perimeter_correct_integer_input(self):
        res = perimeter(81)
        self.assertEqual(res, 508.93800988154646)

    def test_perimeter_correct_float_input(self):
        res = perimeter(101.23432)
        self.assertEqual(res, 636.0739920063165)

    def test_perimeter_invalid_type_input_1(self):
        res = perimeter("1")
        self.assertEqual(res, "Invalid parameters.")

    def test_perimeter_invalid_type_input_2(self):
        res = perimeter("a")
        self.assertEqual(res, "Invalid parameters.")

    def test_perimeter_invalid_type_input_3(self):
        res = perimeter([1, 2, 3])
        self.assertEqual(res, "Invalid parameters.")

    def test_perimeter_invalid_negative_input(self):
        res = perimeter(-2)
        self.assertEqual(res, "Invalid parameters.")
