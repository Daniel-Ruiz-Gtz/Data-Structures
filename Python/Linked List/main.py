class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Return True if the linked list is empty, False otherwise."""
        return self.head is None

    def append(self, data):
        """Append the specified data to the end of the linked list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def prepend(self, data):
        """Prepend the specified data to the beginning of the linked list."""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def delete(self, data):
        """Delete the first occurrence of the specified data from the linked list."""
        if not self.is_empty():
            if self.head.data == data:
                self.head = self.head.next_node
            else:
                current_node = self.head
                while current_node.next_node and current_node.next_node.data != data:
                    current_node = current_node.next_node
                if current_node.next_node:
                    current_node.next_node = current_node.next_node.next_node

    def display(self):
        """Display the elements of the linked list."""
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next_node
        print("Linked List:", elements)

def main():
    # Create a linked list
    my_linked_list = LinkedList()

    # Append elements
    print("Append data: 1")
    my_linked_list.append(1)
    print("Append data: 2")
    my_linked_list.append(2)
    print("Append data: 3")
    my_linked_list.append(3)

    # Prepend elements
    print("Prepend data: 0")
    my_linked_list.prepend(0)

    # Display the linked list
    my_linked_list.display()

    # Delete an element
    print("Delete data: 2")
    my_linked_list.delete(2)

    # Display the modified linked list
    my_linked_list.display()

if __name__ == "__main__":
    main()
