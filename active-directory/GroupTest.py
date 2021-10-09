import unittest

from Group import Group
from Group import is_user_in_group


class GroupTest(unittest.TestCase):

    def test_if_user_is_in_group(self):
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")

        sub_child_user = "sub_child_user"
        sub_child.add_user(sub_child_user)

        child.add_group(sub_child)
        parent.add_group(child)

        self.assertTrue(is_user_in_group(sub_child_user, sub_child))
        self.assertTrue(is_user_in_group(sub_child_user, child))
        self.assertTrue(is_user_in_group(sub_child_user, parent))

    def test_if_user_is_not_in_group(self):
        group = Group("parent")
        user = "user"

        self.assertFalse(is_user_in_group(user, group))