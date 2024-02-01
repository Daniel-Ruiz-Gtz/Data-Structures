class GraphNode:
    def __init__(self, data):
        self.data = data
        self.edges = []

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, data):
        """Add a new node with the specified data to the graph."""
        new_node = GraphNode(data)
        self.nodes.append(new_node)

    def add_edge(self, node1, node2):
        """Add an edge between the nodes node1 and node2 in the graph."""
        if node1 in self.nodes and node2 in self.nodes:
            node1.edges.append(node2)
            node2.edges.append(node1)

    def remove_node(self, data):
        """Remove the node with the specified data from the graph, along with its incident edges."""
        node_to_remove = next((node for node in self.nodes if node.data == data), None)
        if node_to_remove:
            self.nodes.remove(node_to_remove)
            for node in self.nodes:
                node.edges = [edge for edge in node.edges if edge != node_to_remove]

    def remove_edge(self, node1, node2):
        """Remove the edge between the nodes node1 and node2 from the graph."""
        if node1 in self.nodes and node2 in self.nodes:
            node1.edges = [edge for edge in node1.edges if edge != node2]
            node2.edges = [edge for edge in node2.edges if edge != node1]

    def display(self):
        """Display the nodes and edges of the graph."""
        for node in self.nodes:
            edges = [edge.data for edge in node.edges]
            print(f"Node {node.data} - Edges: {edges}")

def main():
    # Create a graph
    my_graph = Graph()

    # Add nodes
    print("Add node: A")
    my_graph.add_node("A")
    print("Add node: B")
    my_graph.add_node("B")
    print("Add node: C")
    my_graph.add_node("C")

    # Add edges
    print("Add edge: A - B")
    my_graph.add_edge(my_graph.nodes[0], my_graph.nodes[1])
    print("Add edge: B - C")
    my_graph.add_edge(my_graph.nodes[1], my_graph.nodes[2])

    # Display the graph
    my_graph.display()

    # Remove a node
    print("Remove node: B")
    my_graph.remove_node("B")

    # Display the modified graph
    my_graph.display()

if __name__ == "__main__":
    main()