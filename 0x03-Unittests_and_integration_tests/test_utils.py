#!/usr/bin/env python3
"""test_utils.py"""

import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator"""

    def test_memoize(self):
        """Test that memoize caches method results"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            instance = TestClass()

            # First call should invoke a_method
            result1 = instance.a_property

            # Second call should use cached value
            result2 = instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Ensure a_method was called only once
            mock_method.assert_called_once()

