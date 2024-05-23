#!/usr/bin/python3
""" LFU caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    Least Frequency Used (LFU) Cache implementation.
    """

    def __init__(self):
        super().__init__()
        self.frequency = {}

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

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq_key = min(self.frequency, key=self.frequency.get)
            if min_freq_key in self.cache_data:
                del self.cache_data[min_freq_key]
                del self.frequency[min_freq_key]
                print("DISCARD: {}".format(min_freq_key))
        self.cache_data[key] = item
        self.frequency[key] = 1

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

        self.frequency[key] += 1

        return self.cache_data[key]
