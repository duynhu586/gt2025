import heapq

def createAdjMatrix():
    size = 13
    matrix = [[0] * size for _ in range(size)]

    edges = [
        ('A', 'B', 4), ('A', 'C', 1),
        ('B', 'F', 3),
        ('C', 'F', 7), ('C', 'D', 8),
        ('D', 'H', 5),
        ('F', 'H', 1), ('F', 'E', 1),
        ('E', 'H', 2), ('E', 'L', 2),
        ('H', 'G', 3), ('H', 'M', 7), ('H', 'L', 6),
        ('G', 'L', 4), ('G', 'M', 4),
        ('L', 'M', 4)
    ]

    # Helper function to convert a character to an index
    def charToIndex(c):
        return ord(c) - ord('A')

    for u, v, w in edges:
        uIndex = charToIndex(u)
        vIndex = charToIndex(v)
        matrix[uIndex][vIndex] = w
        matrix[vIndex][uIndex] = w  # For undirected graph

    return matrix


def displayAdjMatrix(matrix):
    print("Weighted Adjacency Matrix:")
    for row in matrix:
        print(" ".join(f"{cell:2}" for cell in row))

def dijkstra(matrix, start, end):
    n = len(matrix)  # Number of nodes
    distances = [float('inf')] * n  # Initialize distances as infinity
    distances[start] = 0  # Distance to the source is 0
    prevNodes = [-1] * n  # To store the shortest path
    visited = [False] * n  # Track visited nodes
    minHeap = [(0, start)]  # Min-heap to prioritize nodes by distance

    while minHeap:
        curr_distance, curr_node = heapq.heappop(minHeap)

        if visited[curr_node]:
            continue
        visited[curr_node] = True

        for neighbor in range(n):
            if matrix[curr_node][neighbor] > 0:  # Check for an edge
                new_distance = curr_distance + matrix[curr_node][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    prevNodes[neighbor] = curr_node
                    heapq.heappush(minHeap, (new_distance, neighbor))

    # Reconstruct the shortest path
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = prevNodes[current]
    path.reverse()

    return path, distances[end]


def charToIndex(c):
    return ord(c) - ord('A')


def indexToChar(i):
    return chr(i + ord('A'))


if __name__ == "__main__":
    adjMatrix = createAdjMatrix()
    displayAdjMatrix(adjMatrix)

    try:
        startChar = input("\nEnter the source node (A-M): ").upper()
        endChar = input("Enter the target node (A-M): ").upper()

        start = charToIndex(startChar)
        end = charToIndex(endChar)

        if 0 <= start < len(adjMatrix) and 0 <= end < len(adjMatrix):
            path, total_weight = dijkstra(adjMatrix, start, end)
            path_chars = [indexToChar(node) for node in path]

            print("\nDijkstra's Algorithm Result:")
            print(f"Shortest path from {startChar} to {endChar}: {' -> '.join(path_chars)}")
            print(f"Total weight: {total_weight}")
        else:
            print("Invalid input! Please enter nodes within A-L.")
    except Exception as e:
        print(f"Error: {e}")

