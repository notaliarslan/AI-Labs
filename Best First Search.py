from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):
        print("Given Graph", self.graph)

    def BFS(self, s, e):
        visited = []
        queue = []
        path = []
        visited.append(s)
        queue.append(s)
        while queue:
            node = self.MinNode(queue)
            path.append(node)
            queue.remove(node)
            if node == e:
                break
            else:
                for adjacent in self.graph[node]:
                    if adjacent not in visited:
                        visited.append(adjacent)
                        queue.append((adjacent))

        print("Path is : " + str(path))
    def MinNode(self, queue):
        min = 9999
        for x in queue:
            y = huristic[x]
            if y < min:
                min = y;
                node = x;
        return node



g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'D')
g.addEdge('B', 'E')
g.addEdge('B', 'F')
g.addEdge('C', 'G')
g.addEdge('C', 'H')
g.addEdge('D', 'I')
g.addEdge('E', 'J')
g.addEdge('E', 'K')
g.addEdge('G', 'L')
g.addEdge('G', 'M')
g.addEdge('G', 'N')
huristic = \
    {'A': 30,
     'B': 25,
     'C': 28,
     'D': 22,
     'E': 19,
     'F': 16,
     'G': 10,
     'H': 19,
     'I': 9,
     'J': 7,
     'K': 6,
     'L': 3,
     'M': 0,
     'N': 4,
     }

print("heuristic Values", huristic)
g.BFS('A', 'M')
