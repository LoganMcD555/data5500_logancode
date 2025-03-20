import networkx as nx

def count_nodes(graph: nx.Graph) -> int:
    """
    Returns the number of nodes in the given NetworkX graph.

    Parameters:
    graph (nx.Graph): The input NetworkX graph.

    Returns:
    int: The total number of nodes in the graph.
    """
    return graph.number_of_nodes()

# Example usage:
if __name__ == "__main__":
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4, 5])  
    print(count_nodes(G)) 








'''
AI promt: Write a Python function that takes a NetworkX graph as input and returns the number of nodes in the graph.
The function should:
- Accept a NetworkX graph as a parameter.
- Use the built-in NetworkX method to count the nodes.
- Return the total number of nodes.
'''