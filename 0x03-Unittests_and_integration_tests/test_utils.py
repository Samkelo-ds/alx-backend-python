#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient  # Make sure this import matches your actual client module


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient.org method."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the expected value and get_json is called correctly."""
        # Arrange: Setup the mock to return a dummy dictionary
        expected_payload = {"login": org_name, "id": 12345}
        mock_get_json.return_value = expected_payload

        # Act: Create client and call org()
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert: Check get_json was called once with correct URL and org returns expected data
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_payload)

