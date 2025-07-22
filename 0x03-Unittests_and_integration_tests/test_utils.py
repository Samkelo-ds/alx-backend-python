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

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            instance = TestClass()
            first = instance.a_property
            second = instance.a_property
            self.assertEqual(first, 42)
            self.assertEqual(second, 42)
            



