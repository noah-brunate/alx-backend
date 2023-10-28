#!/usr/bin/python3
"""
Module describes the class FIFOCache
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class inherites from BaseCaching
        - is a caching system
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """

        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                target = 1
                for k in sorted(self.cache_data.keys()):
                    if target == 1:
                        print(f"DISCARD: {k}")
                        del self.cache_data[k]
                        target = 0

    def get(self, key):
        """ Get an item by key
        """

        if key in self.cache_data.keys():
            return self.cache_data[key]

        return None
