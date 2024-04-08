class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError('Invalid input: None or single node list')
    first = Node()
    second = Node()
    current = head
    first_head = first
    second_head = second
    while current:
        first.next = current
        first = first.next
        current = current.next
        if current:
            second.next = current
            second = second.next
            current = current.next
    first.next = None
    second.next = None
    return Context(first_head.next, second_head.next)