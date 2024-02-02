class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        """Compute the hash value for the given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the Hash Table."""
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    self.table[index][i] = (key, value)
                    break
            else:
                self.table[index].append((key, value))

    def get(self, key):
        """Return the value associated with the specified key."""
        index = self.hash_function(key)
        if self.table[index] is not None:
            for existing_key, value in self.table[index]:
                if existing_key == key:
                    return value
        raise KeyError(f"Key not found: {key}")

    def delete(self, key):
        """Delete the key-value pair with the specified key from the Hash Table."""
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]
                    break
            else:
                raise KeyError(f"Key not found: {key}")

def main():
    # Create a hash table
    my_hash_table = HashTable(size=10)

    # Insert key-value pairs
    print("Insert key-value pair: ('Alice', 25)")
    my_hash_table.insert("Alice", 25)
    print("Insert key-value pair: ('Bob', 30)")
    my_hash_table.insert("Bob", 30)

    # Get values
    print("Get value for key 'Alice':", my_hash_table.get("Alice"))

    # Delete a key-value pair
    print("Delete key-value pair with key 'Bob'")
    my_hash_table.delete("Bob")

    # Try to get the deleted value (will raise KeyError)
    # my_hash_table.get("Bob")

if __name__ == "__main__":
    main()