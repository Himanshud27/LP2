n = int(input("Enter number of nodes: "))
graph = {}

# Input graph
for i in range(1, n + 1):
    edges = int(input(f"Enter number of edges for node {i}: "))
    graph[i] = []
    for j in range(1, edges + 1):
        node = int(input(f"Enter edge {j} for node {i}: "))
        graph[i].append(node)

# DFS function
def dfs(visited, graph, node):
    if node not in visited: 
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# BFS function
def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Initialize visited sets and queue
visited1 = set()
visited2 = set()
queue = []

# Start traversals from a user-defined node
start_node = int(input("Enter start node: "))

print("\nDFS Traversal:")
dfs(visited1, graph, start_node)

print("\n\nBFS Traversal:")
bfs(visited2, graph, start_node, queue)
