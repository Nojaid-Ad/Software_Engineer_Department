class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data): # used to add a new node
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):  # Pre-  add a new node before the pointed  node
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data): # # Pre-  add a new node after the pointed  node
        if not prev_node:
            print("Previous node is not in the list.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(4)
    linked_list.print_list()  # Output: 1 -> 2 -> 4 -> None
    linked_list.insert_after_node(linked_list.head.next, 3)
    linked_list.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> None
    linked_list.prepend(0)
    linked_list.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> 4 -> None
