#!/usr/bin/python3
"""
module describes the BasicCache class
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class inherite from BaseChing
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

    def get(self, key):
        """ Get an item by key
        """

        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None
