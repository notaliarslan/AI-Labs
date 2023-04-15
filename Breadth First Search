from collections import defaultdict


class lab1:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, f, l):
        visited = []
        non_visited = []
        visited.append(f)
        non_visited.append(f)
        while non_visited:
            n = non_visited.pop(0)
            print(n)
            if (n == l):
                break

            for i in self.graph[n]:
                if i not in visited:
                    visited.append(i)
                    non_visited.append(i)


g = lab1()
s = input("Enter Starting Node: ")
d = input("Enter Ending Node: ")
g.addEdge('LA', 'Seattle')
g.addEdge('LA', 'Dallas')
g.addEdge('LA', 'Chicago')
g.addEdge('LA', 'Atlanta')

g.addEdge('Seattle', 'LA')
g.addEdge('Seattle', 'Dallas')
g.addEdge('Seattle', 'Chicago')
g.addEdge('Seattle', 'Atlanta')

g.addEdge('Dallas', 'LA')
g.addEdge('Dallas', 'Seattle')
g.addEdge('Dallas', 'Atlanta')
g.addEdge('Dallas', 'Chicago')

g.addEdge('Atlanta', 'LA')
g.addEdge('Atlanta', 'Chicago')
g.addEdge('Atlanta', 'Dallas')
g.addEdge('Atlanta', 'Seattle')

g.addEdge('Chicago', 'LA')
g.addEdge('Chicago', 'Seattle')
g.addEdge('Chicago', 'Atlanta')
g.addEdge('Chicago', 'Dallas')


g.bfs(s, d)
