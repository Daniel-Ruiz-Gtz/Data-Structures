class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add the specified item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack."""
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        """Return the item at the top of the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return not bool(self.items)

def main():
    # Create a stack
    my_stack = Stack()

    # Push elements onto the stack
    print("Push item: 1")
    my_stack.push(1)
    print("Push item: 2")
    my_stack.push(2)
    print("Push item: 3")
    my_stack.push(3)

    # Pop elements from the stack
    popped_item = my_stack.pop()
    print("Popped item:", popped_item)

    popped_item = my_stack.pop()
    print("Popped item:", popped_item)

    # Peek at the top element
    top_item = my_stack.peek()
    print("Top item:", top_item)

    # Check if the stack is empty
    is_empty = my_stack.is_empty()
    print("Is the stack empty?", is_empty)

if __name__ == "__main__":
    main()
