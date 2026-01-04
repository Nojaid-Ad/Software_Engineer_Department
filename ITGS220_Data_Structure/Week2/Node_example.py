class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Example usage:
# Creating nodes
node1 = Node(5)
node2 = Node(10)
node3 = Node(15)

# Linking nodes
node1.next = node2
node2.next = node3

# Traversing the linked list
current_node = node1
while current_node is not None:
    print(current_node.data)
    current_node = current_node.next
