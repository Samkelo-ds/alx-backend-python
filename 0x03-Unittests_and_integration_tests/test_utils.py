#!/usr/bin/env python3
"""Unit tests for functions in utils.py."""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test correct return value from access_nested_map."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
["class TestMemoize(unittest.TestCase", "def test_memoize(self"] - test_utils.py doesn't contain: ["class TestMemoize(TestCase", "def test_memoize(self"] - 

