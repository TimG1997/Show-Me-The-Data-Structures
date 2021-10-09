class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def __len__(self):
        return self.size()

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def append_all(self, values):
        for value in values:
            self.append(value)

    def contains(self, value):
        curr_el = self.head

        while curr_el is not None:
            if curr_el.value == value:
                return True
            curr_el = curr_el.next

        return False

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_set(self):
        new_set = set()

        curr_node = self.head

        while curr_node is not None:
            new_set.add(curr_node.value)
            curr_node = curr_node.next

        return new_set


def union(llist_1, llist_2):
    union_set = llist_1.to_set() | llist_2.to_set()

    union_list = LinkedList()

    for element in union_set:
        union_list.append(element)

    return union_list


def intersection(llist_1, llist_2):
    intersection_set = llist_1.to_set() & llist_2.to_set()

    linked_list = LinkedList()

    for element in intersection_set:
        linked_list.append(element)

    return linked_list