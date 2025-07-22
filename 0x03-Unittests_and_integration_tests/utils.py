#!/usr/bin/env python3
"""utils.py"""

from functools import wraps


def memoize(method):
    """Decorator to cache method results."""
    attr_name = "_{}".format(method.__name__)

    @property
    @wraps(method)
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)

    return wrapper




