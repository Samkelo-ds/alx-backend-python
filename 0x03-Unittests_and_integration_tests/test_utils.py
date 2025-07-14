#!/usr/bin/env python3
"""Tests for the access_nested_map function"""

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """This class tests if access_nested_map works correctly."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),  # Go into "a" and get 1
        ({"a": {"b": 2}}, ("a",), {"b": 2}),  # Go into "a" and get {"b": 2}
        ({"a": {"b": 2}}, ("a", "b"), 2),  # Go into "a", then "b", and get 2
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Check if access_nested_map gives the right answer."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

