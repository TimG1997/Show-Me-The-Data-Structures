import unittest

from lru.LRUCache import LRUCache


class LRUCacheTest(unittest.TestCase):

    def test_get(self):
        cache = LRUCache(5)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)

        self.assertEqual(1, cache.get(1))
        self.assertEqual(2, cache.get(2))
        self.assertEqual(-1, cache.get(9))

        cache.set(5, 5)
        cache.set(6, 6)

        self.assertEqual(-1, cache.get(3))