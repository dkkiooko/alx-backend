#!/usr/bin/python3
""" caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ caching system that inherits """
    def __init__(self):
        """ inherits fully """
        super().__init__()

    def put(self, key, item):
        """ assign to dictionary """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ get value linked to key"""
        try:
            return self.cache_data[key]
        except Exception:
            return None
