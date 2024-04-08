class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def get_nth(node, index):
    if node is None:
        raise ValueError('None')
    if index == 0:
        return node
    return get_nth(node.next, index - 1)
