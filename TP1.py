from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)

    def addEdge(self, source, destination):
        self.edges[source].append(destination)

    def isPath(self, start, target):
        visitedNodes = set()
        nodesToVisit = deque([start])

        while nodesToVisit:
            current_node = nodesToVisit.popleft()

            if current_node == target:
                return True

            visitedNodes.add(current_node)
            
            for neighbor in self.edges[current_node]:
                if neighbor not in visitedNodes and neighbor not in nodesToVisit:
                    nodesToVisit.append(neighbor)

        return False

graph = Graph()

edgeList = [
    (1, 2), (2, 5), (3, 6), (4, 6), (6, 7), (4, 7)
]

for src, dest in edgeList:
    graph.addEdge(src, dest)

start = int(input("Start node: "))
target = int(input("End node: "))

if graph.isPath(start, target):
    print("Existed")
else:
    print("Do not exist")
