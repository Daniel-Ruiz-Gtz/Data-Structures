# Hash Table

A Hash Table is a data structure that stores key-value pairs, where each key is mapped to a unique index in the underlying array using a hash function.

## Implementation

The Hash Table implementation in this repository consists of an array and a method for handling collisions (e.g., chaining).

## Methods

### `__init__(size)`

Initializes a new Hash Table with the specified size.

### `hash_function(key)`

Computes the hash value for the given key.

### `insert(key, value)`

Inserts a key-value pair into the Hash Table.

### `get(key)`

Returns the value associated with the specified key.

### `delete(key)`

Deletes the key-value pair with the specified key from the Hash Table.
