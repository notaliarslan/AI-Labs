from collections import defaultdict
from itertools import permutations

class Graph:
    cost=[]
    def __init__(self):
        self.graph = defaultdict(list)
        self.costs=[]
        self.shortest = 0
        self.paths=[]
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):
        print(self.graph)

    def findactualpathvalue(self):
        path_cost = 0
        tsp=actualvalues
        per=permutations(self.graph.keys())
        for i in list (per):
            if i[0] == "A":
                i=list(i)
                i.append('A')
                print(i)
                for j in range(len(i)-1):
                    path_cost = path_cost + tsp[i[j]+i[j+1]]
            if path_cost != 0:
                print("Path cost is: ", path_cost)
                self.costs.append(path_cost)
            path_cost = 0
        return path_cost

    def hillclimbing(self, minimum):
        for x in range(len(self.costs)-1):
            current = self.costs[x]
            next_value = self.costs[x+1]
            if current <= next_value:
                minimum = current
                self.shortest = x
            else:
                break
        print('\nMinimum path from the above mentioned paths is: ', minimum)

g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('A', 'D')
g.addEdge('B', 'A')
g.addEdge('B', 'C')
g.addEdge('B', 'D')
g.addEdge('C', 'A')
g.addEdge('C', 'B')
g.addEdge('C', 'D')
g.addEdge('D', 'A')
g.addEdge('D', 'B')
g.addEdge('D', 'C')

actualvalues = \
    {'AB': 25,
     'AD': 15,
     'BD': 45,
     'BC': 10,
     'CD': 5,
     'AC': 10,
     'BA': 25,
     'DA': 15,
     'DB': 45,
     'CB': 10,
     'DC': 5,
     'CA': 10,
     }
g.findactualpathvalue()
minimum = float('inf')
g.hillclimbing(minimum)
