import heapq

def createAdjMatrix():
    size = 9
    matrix = [[0] * size for _ in range(size)]
    edges = [
        (1, 2, 4), (1, 5, 1), (1, 7, 2),
        (2, 3, 7), (2, 6, 5),
        (3, 4, 1), (3, 6, 8),
        (4, 6, 6), (4, 7, 4), (4, 8, 3),
        (5, 6, 9), (5, 7, 10),
        (6, 9, 2),
        (7, 9, 8),
        (8, 9, 1),
        (9, 8, 7)
    ]
    for u, v, w in edges:
        matrix[u - 1][v - 1] = w
        matrix[v - 1][u - 1] = w
    return matrix

def displayAdjMatrix(matrix):
    print("Weighted Adjacency Matrix:")
    for row in matrix:
        print(" ".join(f"{cell:2}" for cell in row))

def primAlgorithm(matrix, start):
    n = len(matrix)
    visited = [False] * n
    minHeap = [(0, start, -1)]
    mstEdges = []
    totalWeight = 0

    while minHeap:
        weight, node, parent = heapq.heappop(minHeap)
        if visited[node]:
            continue
        visited[node] = True
        totalWeight += weight

        if parent != -1:
            mstEdges.append((parent + 1, node + 1, weight))

        for neighbor in range(n):
            if not visited[neighbor] and matrix[node][neighbor] > 0:
                heapq.heappush(minHeap, (matrix[node][neighbor], neighbor, node))

    return mstEdges, totalWeight

def kruskalAlgorithm(matrix):
    n = len(matrix)
    edges = [
        (matrix[i][j], i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if matrix[i][j] > 0
    ]
    edges.sort()
    parent = list(range(n))
    rank = [0] * n
    mstEdges = []
    totalWeight = 0

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mstEdges.append((u + 1, v + 1, weight))
            totalWeight += weight

    return mstEdges, totalWeight

if __name__ == "__main__":
    adjMatrix = createAdjMatrix()
    displayAdjMatrix(adjMatrix)

    try:
        start_node = int(input("\nEnter the root node (1-9): ")) - 1
        print("\nPrim's Algorithm:")
        prim_edges, prim_weight = primAlgorithm(adjMatrix, start_node)
        print("Edges in MST:", prim_edges)
        print("Total Weight of MST:", prim_weight)

        print("\nKruskal's Algorithm:")
        kruskal_edges, kruskal_weight = kruskalAlgorithm(adjMatrix)
        print("Edges in MST:", kruskal_edges)
        print("Total Weight of MST:", kruskal_weight)
    except ValueError:
        print("Invalid input! Please enter an integer.")
