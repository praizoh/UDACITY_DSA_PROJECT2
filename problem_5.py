import hashlib
import datetime


def get_timestamp():
    return datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __repr__(self):
        return f'Timestamp: {self.timestamp} \nData: {self.data} \nSHA256 Hash: {self.hash} \nPrev_Hash: {self.previous_hash}'


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
        self.tail = None

    def append(self, value):
        """ Append a node to the end of the list """
        # Here I'm not keeping track of the tail. It's possible to store the tail
        # as well as the head, which makes appending like this an O(1) operation.
        # Otherwise, it's an O(N) operation as you have to iterate through the
        # entire list to add a new tail.

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


block_a = Block(get_timestamp(), "Block A", 0)
block_b = Block(get_timestamp(), "Block B", block_a.hash)
block_c = Block(get_timestamp(), "Block C", block_b.hash)

linked_list = LinkedList()
(linked_list.append(block_a))
linked_list.append(block_b)
linked_list.append(block_c)
print(linked_list.to_list())
