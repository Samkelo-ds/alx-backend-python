#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map 
from client import GithubOrgClient  # Adjust import path as per your project structure

class TestAccessNestedMap(unittest.TestCase):
    """Test the access_nested_map function."""

    @parameterized.expand([
        ({"a": {"b": 1}}, ("a", "b"), 1),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ({"a": {"b": {"c": 3}}}, ("a", "b", "c"), 3),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the expected value."""
         # Adjust import path as per your project structure
        self.assertEqual(access_nested_map(nested_map, path), expected)

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
     ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        self.assertRaiseException(test_access_nested_map(nested_map, path), expected):

 

class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that org() returns the expected result."""
        expected_payload = {"some": "data"}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org()

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_payload)


