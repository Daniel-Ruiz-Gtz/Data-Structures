class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add the specified item to the rear of the queue."""
        self.items.insert(0, item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.is_empty():
            return self.items.pop()

    def front(self):
        """Return the item at the front of the queue without removing it."""
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return not bool(self.items)

def main():
    # Create a queue
    my_queue = Queue()

    # Enqueue elements
    print("Enqueue item: 1")
    my_queue.enqueue(1)
    print("Enqueue item: 2")
    my_queue.enqueue(2)
    print("Enqueue item: 3")
    my_queue.enqueue(3)

    # Dequeue elements
    dequeued_item = my_queue.dequeue()
    print("Dequeued item:", dequeued_item)

    dequeued_item = my_queue.dequeue()
    print("Dequeued item:", dequeued_item)

    # Front of the queue
    front_item = my_queue.front()
    print("Front item:", front_item)

    # Check if the queue is empty
    is_empty = my_queue.is_empty()
    print("Is the queue empty?", is_empty)

if __name__ == "__main__":
    main()
