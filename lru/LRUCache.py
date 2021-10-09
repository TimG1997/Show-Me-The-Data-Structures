from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        if capacity is None or capacity <= 0:
            raise ValueError("Please provide a capacity not equal to NULL and greater than zero")

        self.ordered_dict = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.ordered_dict:
            value = self.ordered_dict.pop(key)
            self.ordered_dict[key] = value  # inserts again at the end
            return value
        else:
            return -1

    def set(self, key, value):
        if len(self.ordered_dict) == self.capacity:
            self.ordered_dict.popitem(last=False)  # pops first item = least recently used item

        self.ordered_dict[key] = value
