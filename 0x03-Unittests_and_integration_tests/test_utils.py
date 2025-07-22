from utils import access_nested_map
from parameterized import parameterized
import unittest

class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map."""

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def access_nested_map(nested_map, path):
    """Access value in nested map using path tuple."""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


