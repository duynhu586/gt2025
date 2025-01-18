def disAdjMatrix(graph):
    maxNode = max(graph.keys())
    matrix = [[0] * (maxNode + 1) for _ in range(maxNode + 1)]

    for parent, neighbors in graph.items():
        for neighbor in neighbors:
            matrix[parent][neighbor] = 1

    print("Adjacency Matrix:")
    for row in matrix[1:]:
        print(" ".join(map(str, row[1:])))


def inorderTraversal(node, graph, visited_nodes):
    if node is None or visited_nodes[node]:
        return

    visited_nodes[node] = True
    neighbors = graph.get(node, [])

    if neighbors:
        inorderTraversal(neighbors[0], graph, visited_nodes)

    print(node, end=" ")

    for neighbor in neighbors[1:]:
        inorderTraversal(neighbor, graph, visited_nodes)

if __name__ == "__main__":
    graph_structure = {
        1: [2, 3],
        2: [5, 6],
        3: [4],
        4: [8],
        5: [7],
        6: [],
        7: [],
        8: []
    }
    disAdjMatrix(graph_structure)
    try:
        starting_node = int(input("\nEnter starting node: "))
        visited = [False] * (max(graph_structure.keys()) + 1)
        print("Traversal Output:")
        inorderTraversal(starting_node, graph_structure, visited)
    except ValueError:
        print("Invalid input! Please enter an integer.")
