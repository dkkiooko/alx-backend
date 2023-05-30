#!/usr/bin/python3
""" FIFO caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """caching system"""
    def __init__(self):
        """overload"""
        super().__init__()

    def put(self, key, item):
        """ FIFO put """
        if key is None or item is None:
            return
        if (
            len(self.cache_data) >= self.MAX_ITEMS
                ) and (key not in self.cache_data.keys()):
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")
        self.cache_data[key] = item

    def get(self, key):
        """ FIFO get """
        try:
            return self.cache_data[key]
        except Exception:
            return None
