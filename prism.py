import heapq
from collections import defaultdict

def prim(graph, start):
    mst = []
    visited = set()
    min_edges = [(0, start, None)]

    while min_edges:
        cost, node, parent = heapq.heappop(min_edges)
        if node in visited:
            continue
        visited.add(node)
        if parent is not None:
            mst.append((parent, node, cost))

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_edges, (weight, neighbor, node))
    return mst

# Example usage:
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}
print(prim(graph, 'A'))
