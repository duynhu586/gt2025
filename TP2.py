from collections import defaultdict, deque

def toAdjMatrix(edges, nodeNum):
    adjMatrix = [[0] * nodeNum for _ in range(nodeNum)]
    for src, dest in edges:
        adjMatrix[src - 1][dest - 1] = 1
    return adjMatrix

def printMatrix(adjMatrix):
    print("Adjacency Matrix:")
    for row in adjMatrix:
        print(" ".join(map(str, row)))

def adjToList(adjMatrix):
    adjList = defaultdict(list)
    for i, row in enumerate(adjMatrix):
        for j, value in enumerate(row):
            if value == 1:
                adjList[i + 1].append(j + 1)
    return adjList

def weaklyConnected(adjMatrix):
    adjList = adjToList(adjMatrix)

    # Create an undirected adjacency list
    undirectedAdjList = defaultdict(list)
    for node, neighbors in adjList.items():
        for neighbor in neighbors:
            undirectedAdjList[node].append(neighbor)
            undirectedAdjList[neighbor].append(node)

    visitedNodes = set()
    weakComponentNum = 0

    def bfsComponent(start_node):
        """Explores a connected component using BFS."""
        queue = deque([start_node])
        while queue:
            current = queue.popleft()
            for neighbor in undirectedAdjList[current]:
                if neighbor not in visitedNodes:
                    visitedNodes.add(neighbor)
                    queue.append(neighbor)

    for node in range(1, len(adjMatrix) + 1):
        if node not in visitedNodes:
            weakComponentNum += 1
            visitedNodes.add(node)
            bfsComponent(node)

    return weakComponentNum

def stronglyConnected(adjMatrix):
    adjList = adjToList(adjMatrix)
    visitedNodes = set()
    finishOrder = []

    def dfs_forward(node):
        """Performs a DFS to determine finish order."""
        visitedNodes.add(node)
        for neighbor in adjList[node]:
            if neighbor not in visitedNodes:
                dfs_forward(neighbor)
        finishOrder.append(node)
    for node in range(1, len(adjMatrix) + 1):
        if node not in visitedNodes:
            dfs_forward(node)

    # Build the reversed adjacency list
    reversed_adj_list = defaultdict(list)
    for src, neighbors in adjList.items():
        for neighbor in neighbors:
            reversed_adj_list[neighbor].append(src)
    visitedNodes.clear()
    strong_component_count = 0

    def dfs_reverse(node):
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visitedNodes:
                visitedNodes.add(current)
                stack.extend(reversed_adj_list[current])
    while finishOrder:
        node = finishOrder.pop()
        if node not in visitedNodes:
            strong_component_count += 1
            dfs_reverse(node)
    return strong_component_count

if __name__ == "__main__":
    graphEdges = [
        (1, 2), (1, 4), (2, 3), (2, 6),
        (6, 3), (6, 4), (5, 4), (7, 6),
        (7, 3), (7, 5), (7, 8), (8, 9), (5, 9)
    ]
    nodeCount = 9

    graphAdjMatrix = toAdjMatrix(graphEdges, nodeCount)

    printMatrix(graphAdjMatrix)

    weak_components = weaklyConnected(graphAdjMatrix)
    strong_components = stronglyConnected(graphAdjMatrix)

    print(f"\nNumber of weakly connected components: {weak_components}")
    print(f"Number of strongly connected components: {strong_components}")
