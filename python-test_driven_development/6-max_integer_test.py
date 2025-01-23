#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_regular_case(self):
        """Test a regular case"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test a list with only one element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([100]), 100)

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        """Test a list with both positive and negative numbers"""
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([1, -3, 4, 2]), 4)

    def test_floats(self):
        """Test a list with floats"""
        self.assertEqual(max_integer([1.5, 2.7, 3.2, 4.0]), 4.0)
        self.assertEqual(max_integer([1.5, 3.6, 2.2]), 3.6)

    def test_mixed_integers_and_floats(self):
        """Test a list with both integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.0]), 4.0)
        self.assertEqual(max_integer([1.5, 2, 3.7, 2.5]), 3.7)

if __name__ == "__main__":
    unittest.main()

