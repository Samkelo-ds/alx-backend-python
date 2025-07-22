#!/usr/bin/env python3
"""Utilities Module"""


def access_nested_map(nested_map, path):
    """Access value in nested map using path tuple."""
    for key in path:
        if not isinstance(nested_map, dict):
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map
