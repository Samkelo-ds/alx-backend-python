#!/usr/bin/env python3
"""
test_utils.py
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    """Test utils.get_json using mocked HTTP calls."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")  # Patch requests.get in utils module
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json returns expected payload with mocked requests.get."""
        # Setup the mock to return a response with .json() method returning test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function
        result = get_json(test_url)

        # Assert requests.get was called exactly once with test_url
        mock_get.assert_called_once_with(test_url)

        # Assert the function returns the mocked JSON payload
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
