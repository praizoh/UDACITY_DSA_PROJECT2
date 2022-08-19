import numpy as np


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

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    if (llist_1.head is None):
        return llist_2
    if (llist_2.head is None):
        return llist_1
    list_one = to_list(llist_1)
    list_two = to_list(llist_2)
    union_set = set(list_one + list_two)
    sorted_union_llist = LinkedList()
    for item in sorted(list(union_set)):
        sorted_union_llist.append(item)
    return sorted_union_llist


def intersection(llist_1, llist_2):
    #   get union of lists
    if llist_2.head is None or llist_1.head is None:
        return "There is no intersect"
    combine_list = []
    list_1 = to_list(llist_1)
    list_2 = to_list(llist_2)
    for item in list_1:
        if is_in_list(llist_2, item):
            combine_list.append(item)
    for item in list_2:
        if is_in_list(llist_1, item):
            combine_list.append(item)
    if len(combine_list) == 0:
        return "There is no intersect"

    sorted_intersect_llist = LinkedList()

    for item in sorted(set(list(combine_list))):
        sorted_intersect_llist.append(item)
    return sorted_intersect_llist


def is_in_list(linked_list, value):
    if linked_list.head is None:
        linked_list.head = Node(value)
        return False
    node = linked_list.head
    if node.value == value:
        return True
    while node.next:
        node = node.next
        if node.value == value:
            return True
    return False


def to_list(linked_list):
    out = []
    node = linked_list.head
    while node:
        out.append(node.value)
        node = node.next
    return out


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [9, 0, 0, 4]
element_2 = [9, 33, 9, 2, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))  # 0 -> 1 -> 2 -> 4 -> 9 -> 33 ->
print(intersection(linked_list_1, linked_list_2))  # 9 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_3 = [1, 2, 3, 4, 5, 8, 0, 3, 4, 4]
element_4 = [3, 4, 9, 0, 7]

for i in element_3:
    linked_list_3.append(i)

for i in element_4:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))  # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9 ->
print(intersection(linked_list_3, linked_list_4))  # 0 -> 3 -> 4 ->

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [2, 3, 4]
element_6 = [5, 6, 7]

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))  # 2 -> 3 -> 4 -> 5 -> 6 -> 7 ->
print(intersection(linked_list_5, linked_list_6))  # There is no intersect

# Test Case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_7 = []
element_8 = [1, 7, 8, 9, 11, 21, 1]

for i in element_7:
    linked_list_7.append(i)

for i in element_8:
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8))  # 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 ->
print(intersection(linked_list_7, linked_list_8))  # There is no intersect

# # Test case 5

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_9 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
element_10 = [3, 3, 1, 1, 2, 2]

for i in element_9:
    linked_list_9.append(i)

for i in element_10:
    linked_list_10.append(i)

print(union(linked_list_9, linked_list_10))  # 1 -> 2 -> 3 ->
print(intersection(linked_list_9, linked_list_10))  # 1 -> 2 -> 3 ->
