from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):
        print("Given Graph", self.graph)

    def BFS(self, start, end):
        distance = {}
        visited = []
        queue = []
        path = []
        visited.append(start)
        queue.append(start)
        my_str = '1'
        distance[start] = 0
        while queue:
            node = self.MinNode(queue, distance)
            d1 = distance[node]
            path.append(node)
            queue.remove(node)
            if node == end:
                break
            else:
                for adjacent in self.graph[node]:
                    if adjacent not in visited:
                        p = node + adjacent
                        d = actualvalues[p]
                        distance[adjacent] = d + d1
                        visited.append(adjacent)
                        queue.append(adjacent)

        print("Path is : " + str(path))

    def MinNode(self, queue, distance):

        global node
        min = 9999
        for x in queue:
            y = huristic[x]
            y1 = distance[x]
            if y + y1 < min:
                min = y + y1
                node = x
        return node



# Driver code

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
g.addEdge('H', 'N')
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
actualvalues = \
    {
        'AB': 12,
        'AC': 11,
        'BD': 2,
        'BE': 1,
        'BF': 3,
        'CG': 4,
        'CH': 5,
        'DI': 4,
        'EJ': 4,
        'EK': 4,
        'GL': 4,
        'HN': 4,
        'GM': 4,
    }

print("heuristic Values", huristic)
