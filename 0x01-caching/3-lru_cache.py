#!/usr/bin/env python3
""" LRU caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ implements Least Recently Used Caching """
    def __init__(self):
        """ inititate LRU"""
        super().__init__()
        self.cache = []

    def put(self, key, item):
        """ assign to cache data based on LRU """
        if key and item is not None:
            if key in self.cache_data:
                self.cache.remove(key)
            self.cache_data[key] = item
            self.cache.append(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            lru = self.cache.pop(0)
            self.cache_data.pop(lru)
            print("DISCARD: {}".format(lru))

    def get(self, key):
        """ get value linked to key """
        try:
            self.cache.remove(key)
            self.cache.append(key)
            return self.cache_data.get(key)
        except Exception:
            return None
