class Node:
    def __init__(self, next=None):
        self.next = next


def swap_pairs(head):
    if head is None or head.next is None:
        return head
    n = Node()
    n.next = head
    prev = n

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first

    return n.next
