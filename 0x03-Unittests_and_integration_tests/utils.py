#!/usr/bin/env python3
"""
utils.py
"""

def access_nested_map(nested_map, path):
    """
    Access a nested map with a sequence of keys.
    Raise KeyError if any key is missing or if path is invalid.
    """
    current = nested_map
    for key in path:
        if not isinstance(current, dict):
            raise KeyError(key)
        if key not in current:
            raise KeyError(key)
        current = current[key]
    return current

