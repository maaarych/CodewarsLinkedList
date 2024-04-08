class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Context:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


def move_node(source, dest):
    if source is None:
        raise ValueError('None')
    node_to_move = source
    source = source.next
    if dest is None:
        dest = node_to_move
        dest.next = None
    else:
        node_to_move.next = dest
        dest = node_to_move
    return Context(source, dest)


source = Node(1, Node(2, Node(3)))
dest = Node(4, Node(5, Node(6)))
print(move_node(source, dest).source.data)
print(move_node(source, dest).dest.data)
