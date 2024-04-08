class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def linked_list_from_string(s):
    if s == 'None':
        return None

    values = s.split(" -> ")
    head = Node(int(values[0]))
    current = head

    for value in values[1:]:
        if value == 'None':
            break
        current.next = Node(int(value))
        current = current.next

