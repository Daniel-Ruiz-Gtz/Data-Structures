# Queue

A Queue is a First In, First Out (FIFO) data structure that follows the order of insertion and removal. Elements are added (enqueued) at the rear and removed (dequeued) from the front.

## Implementation

The Queue implementation in this repository uses a Python list to store elements. The front of the queue corresponds to the end of the list.

## Methods

### `enqueue(item)`

Adds the specified item to the rear of the queue.

### `dequeue()`

Removes and returns the item from the front of the queue.

### `front()`

Returns the item at the front of the queue without removing it.

### `is_empty()`

Returns `True` if the queue is empty, `False` otherwise.
