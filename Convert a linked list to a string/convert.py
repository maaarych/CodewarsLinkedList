class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def stringify(self,node):
        if node is None:
            return "None"
        return str(node.data) + " -> " + self.stringify(node.next)

print(Node(1, Node(2, Node(3, Node(4, Node(5))))).stringify(Node(1, Node(2, Node(3, Node(4, Node(5)))))))
