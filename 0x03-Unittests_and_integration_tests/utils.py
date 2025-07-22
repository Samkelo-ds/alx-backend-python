#!/usr/bin/env python3
"""
utils.py
"""

import requests
from typing import Any


def get_json(url: str) -> Any:
    """Make an HTTP GET request to `url` and return the JSON payload."""
    response = requests.get(url)
    return response.json()



