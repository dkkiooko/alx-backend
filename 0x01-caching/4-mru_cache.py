#!/usr/bin/env python3
""" MRU Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Most recently used item algo """
    def __init__(self):
        """ initiate class """
        super().__init__()
        self.cache = []

    def put(self, key, item):
        """ assign values to cache data """
        if key and item is not None:
            if key not in self.cache_data:
                self.cache.append(key)
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            mru = self.cache.pop(-2)
            self.cache_data.pop(mru)
            print("DISCARD: {}".format(mru))

    def get(self, key):
        """ return value linked to key in cache """
        if key is not None and key in self.cache_data:
            self.cache.remove(key)
            self.cache.append(key)
        return self.cache_data.get(key)
