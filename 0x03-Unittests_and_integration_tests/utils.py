#!/usr/bin/env python3
"""Utility functions for nested data access and JSON retrieval."""

from typing import Mapping, Any, Sequence
import requests


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access a value in a nested map using a sequence of keys."""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str) -> dict:
    """Fetch JSON content from a URL."""
    response = requests.get(url)
    return response.json()
