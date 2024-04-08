class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def loop_size(node):
    slow = node.next
    fast = node.next.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    slow = node
    while slow != fast:
        slow = slow.next
        fast = fast.next
    size = 1
    fast = fast.next
    while slow != fast:
        size += 1
        fast = fast.next
    return size
