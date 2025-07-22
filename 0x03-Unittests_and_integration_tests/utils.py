#!/usr/bin/env python3
"""
utils.py
"""

from typing import Any, Mapping, Sequence, Union


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """
    Access a nested map with a sequence of keys.

    Args:
        nested_map (Mapping): Nested dictionary to access.
        path (Sequence): Sequence of keys to traverse.

    Returns:
        Any: Value found at the nested path.

    Raises:
        KeyError: If any key is not found or path is invalid.
    """
    current = nested_map
    for key in path:
        if not isinstance(current, dict):
            raise KeyError(key)
        if key not in current:
            raise KeyError(key)
        current = current[key]
    return current


