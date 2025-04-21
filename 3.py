'''Assignment 3: Kruskal's Algorithm'''
# Disjoint Set Union (Union-Find)
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)

        if u_root == v_root:
            return False  # Already connected

        # Union by rank
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1

        return True


# Kruskal's Algorithm
def kruskal(n, edges):
    ds = DisjointSet(n)
    mst = []
    total_cost = 0

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])  # x = (u, v, weight)

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost


# Example graph
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

num_nodes = 4  # Nodes labeled 0 to 3

mst, cost = kruskal(num_nodes, edges)
print("Edges in MST:", mst)
print("Total cost of MST:", cost)


edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

num_nodes = 4

mst, cost = kruskal(num_nodes, edges)
print("Edges in MST:", mst)
print("Total cost of MST:", cost)
