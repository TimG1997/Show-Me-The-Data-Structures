import unittest

from UnionAndIntersection import LinkedList, intersection, union


class UnionAndIntersectionTest(unittest.TestCase):

    def setUp(self):
        self.list_one = LinkedList()
        self.list_two = LinkedList()

        self.list_one.append_all([3, 2, 4, 35, 6, 65, 6, 4, 3, 21])
        self.list_two.append_all([6, 32, 4, 9, 6, 1, 11, 21, 1])

    def test_contains(self):
        linked_list = LinkedList()
        linked_list.append(1)

        self.assertTrue(linked_list.contains(1))
        self.assertFalse(linked_list.contains(2))

    def test_union(self):
        union_list = union(self.list_one, self.list_two)

        self.assertEqual(11, len(union_list))
        self.assertTrue(union_list.contains(32))
        self.assertTrue(union_list.contains(65))
        self.assertTrue(union_list.contains(2))
        self.assertTrue(union_list.contains(35))
        self.assertTrue(union_list.contains(3))
        self.assertTrue(union_list.contains(4))
        self.assertTrue(union_list.contains(6))
        self.assertTrue(union_list.contains(1))
        self.assertTrue(union_list.contains(9))
        self.assertTrue(union_list.contains(11))
        self.assertTrue(union_list.contains(21))

    def test_intersection(self):
        intersection_list = intersection(self.list_one, self.list_two)

        self.assertEqual(3, len(intersection_list))
        self.assertTrue(intersection_list.contains(4))
        self.assertTrue(intersection_list.contains(21))
        self.assertTrue(intersection_list.contains(6))