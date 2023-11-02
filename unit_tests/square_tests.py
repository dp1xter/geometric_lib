import unittest
from square import *

class SquareTestCase(unittest.TestCase):
    def test_area_correct_integer_input(self):
        res = area(81)
        self.assertEqual(res, 6561)

    def test_area_correct_float_input(self):
        res = area(101.23432)
        self.assertEqual(res, 10248.387545862399)

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
        self.assertEqual(res, 324)

    def test_perimeter_correct_float_input(self):
        res = perimeter(101.23432)
        self.assertEqual(res, 404.93728)

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
