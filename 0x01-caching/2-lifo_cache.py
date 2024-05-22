#!/usr/bin/python3
""" LIFO caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """"""

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.stack:
            self.stack.remove(key)
            self.stack.append(key)
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.stack.pop()
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
