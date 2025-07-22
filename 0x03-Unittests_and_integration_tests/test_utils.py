#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map"""

import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function"""

    def test_access_nested_map(self):
        """Test normal access"""
        self.assertEqual(access_nested_map({"a": 1}, ("a",)), 1)
        self.assertEqual(access_nested_map({"a": {"b": 2}}, ("a",)), {"b": 2})
        self.assertEqual(access_nested_map({"a": {"b": 2}}, ("a", "b")), 2)

    def test_access_nested_map_exception(self):
        """Test access with missing keys"""
        with self.assertRaises(KeyError):
            access_nested_map({}, ("a",))

        with self.assertRaises(KeyError):
            access_nested_map({"a": 1}, ("a", "b"))


if __name__ == '__main__':
    unittest.main()



