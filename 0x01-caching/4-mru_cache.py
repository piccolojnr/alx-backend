#!/usr/bin/python3
""" LIFO caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Most Recently Used (MRU) Cache implementation.
    """

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key: The key of the item.
            item: The item to be added.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key in self.keys:
            self.keys.remove(key)

        if len(self.keys) >= BaseCaching.MAX_ITEMS:
            discard = self.keys.pop()
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """
        Get an item by key.

        Args:
            key: The key of the item.

        Returns:
            The item associated with the key, or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None

        self.keys.remove(key)
        self.keys.append(key)

        return self.cache_data[key]
