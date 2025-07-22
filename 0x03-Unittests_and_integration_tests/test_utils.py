#!/usr/bin/env python3
"""
test_utils.py
"""

import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map returns correct result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    def test_access_nested_map_exception(self):
        """
        Test access_nested_map raises KeyError with missing keys.
        """
        with self.assertRaises(KeyError):
            access_nested_map({}, ("a",))

        with self.assertRaises(KeyError):
            access_nested_map({"a": 1}, ("a", "b"))



