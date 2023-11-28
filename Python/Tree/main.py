class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        """Return True if the binary tree is empty, False otherwise."""
        return self.root is None

    def insert(self, data):
        """Insert the specified data into the binary tree."""
        if self.is_empty():
            self.root = TreeNode(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, current_node):
        """Helper method for recursive insertion."""
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(data)
            else:
                self._insert_recursive(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = TreeNode(data)
            else:
                self._insert_recursive(data, current_node.right)

    def search(self, data):
        """Return True if the specified data is found in the binary tree, False otherwise."""
        return self._search_recursive(data, self.root) if not self.is_empty() else False

    def _search_recursive(self, data, current_node):
        """Helper method for recursive search."""
        if current_node is None:
            return False
        elif data == current_node.data:
            return True
        elif data < current_node.data:
            return self._search_recursive(data, current_node.left)
        else:
            return self._search_recursive(data, current_node.right)

    def display(self):
        """Display the elements of the binary tree using an in-order traversal."""
        elements = []
        self._display_recursive(self.root, elements)
        print("Binary Tree:", elements)

    def _display_recursive(self, current_node, elements):
        """Helper method for recursive in-order traversal."""
        if current_node:
            self._display_recursive(current_node.left, elements)
            elements.append(current_node.data)
            self._display_recursive(current_node.right, elements)

def main():
    # Create a binary tree
    my_binary_tree = BinaryTree()

    # Insert elements
    print("Insert data: 5")
    my_binary_tree.insert(5)
    print("Insert data: 3")
    my_binary_tree.insert(3)
    print("Insert data: 7")
    my_binary_tree.insert(7)

    # Display the binary tree
    my_binary_tree.display()

    # Search for an element
    search_result = my_binary_tree.search(3)
    print("Search result for data 3:", search_result)

    search_result = my_binary_tree.search(10)
    print("Search result for data 10:", search_result)

if __name__ == "__main__":
    main()
