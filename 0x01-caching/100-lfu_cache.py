#!/usr/bin/env python3
"""
Module describes the LFUCache class
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ class in herites from BseCaching
        - is a caching system
    """

    def __init__(self):
        super().__init__()
        self.cache_items = {}

    def put(self, key, item):
        """ Add an item in the cache
        """

        if key is None or item is None:
            pass
        else:
            if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                sorted_list = sorted(self.cache_items.items(),
                                     key=lambda x: x[1])
                k, v = sorted_list[0]
                print(f"DISCARD: {k}")
                del self.cache_data[k]
                del self.cache_items[k]

            self.cache_data[key] = item

            if key in self.cache_items.keys():
                self.cache_items[key] += 1
            else:
                self.cache_items[key] = 0

    def get(self, key):
        """ Get an item by key
        """

        if key in self.cache_data.keys():
            self.cache_items[key] += 1
            return self.cache_data[key]

        return None
