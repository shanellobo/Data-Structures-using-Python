class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly Linked List
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Append at end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Insert at given position (1-based index)
    def insert_at_position(self, data, position):
        if position < 1:
            print("Position must be >= 1")
            return
       
        new_node = Node(data)

        # Insert at beginning
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 1

        # Move to node before insertion point
        while current is not None and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of range")
            return

        new_node.next = current.next
        current.next = new_node

    # Traverse
    def traverse(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
ll= SinglyLinkedList()

ll.append(10)
ll.append(20)
ll.append(40)
print("After appending at the end:")
ll.traverse()

ll.insert_at_beginning(5)
print("After inserting at the beginning:")
ll.traverse()

ll.insert_at_position(30, 4) # Insert at 4th position
print("After inserting 30 at position 4:")
ll.traverse()

ll.insert_at_position(1, 1) # Insert at first position
print("After inserting 1 at position 1:")
ll.traverse()

ll.insert_at_position(99, 10)