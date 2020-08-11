class graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

# Check for the visited and unvisited nodes
def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

# Check for the visited and unvisited nodes
def printDfs(graph, root):
    visited = set([root])
    performDfs(graph, root, visited)
    

def performDfs(graph, node, visited):
    visited.add(node)
    print(node)
    for next in graph[node] - visited:
        performDfs(graph, next, visited)
    return


gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }


dfs(gdict, 'a')
printDfs(gdict, 'a')