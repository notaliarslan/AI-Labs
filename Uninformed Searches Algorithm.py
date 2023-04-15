from collections import defaultdict


class lab1:
    def __init__(self):
        self.visited = []
        self.non_visited = []
        self.graph = defaultdict(list)
        self.found = False
        self.check = False

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

    def dfs(self, f, l):
        print(f)
        if f == l:
            self.found = True
        self.visited.append(f)
        for x in self.graph[f]:
            if x not in self.visited and self.found == False:
                self.dfs(x, l)
            else:
                return

    def dls(self, f, l, d):
        if f not in self.visited:
            print("{}".format(f))
            self.visited.append(f)
        if f == l:
            self.check = True
            return True
        if d <= 0:
            return False
        for i in self.graph[f]:
            if self.dls(i, l, d - 1) == True:
                return True
        return False

    def ids(self, f, l):
        for i in range(0, 4):
            self.visited.clear()
            if self.dls(f, l, i) == True:
                return True
        return False


g = lab1()

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('A', 'D')
g.addEdge('A', 'E')

g.addEdge('B', 'F')
g.addEdge('B', 'G')

g.addEdge('G', 'K')
g.addEdge('G', 'L')

g.addEdge('L', 'O')

g.addEdge('C', 'H')

g.addEdge('D', 'I')
g.addEdge('D', 'J')

g.addEdge('I', 'M')

g.addEdge('J', 'N')


print("1. BFS ")
print("2. DFS ")
print("3. DLS ")
print("4. IDS ")
choice = input("Choice: ")
print()
s = input("Enter Starting Node: ")
d = input("Enter Ending Node: ")
depth = 2
if choice == "BFS":
    g.bfs(s, d)
elif choice == "DFS":
    g.dfs(s, d)
elif choice == "DLS":
    g.dls(s, d, depth)
    print("DFS Traversal to {}  ".format(d))
    if g.check == False:
        print()
        print("{} is not reachable with Depth: {}".format(d, depth))
    else:
        print()
        print("{} is reachable with Depth: {}".format(d, depth))
elif choice == "IDS":
    print("3. Iterative Deepening Search Traversal to {}:  ".format(d))
    g.ids(s, d)
    if g.check == False:
        print()
        print("{} is not reachable ".format(d))
    else:
        print()
        print("{} is reachable ".format(d))
