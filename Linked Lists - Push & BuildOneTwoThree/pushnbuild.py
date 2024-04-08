class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def build_one_two_three():
    head = None
    head = push(head, 1)
    head = push(head, 2)
    head = push(head, 3)
    head = reverse_linked_list(head)
    return head

