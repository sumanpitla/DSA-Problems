from typing import List
import heapq

class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def spanningTree(self, V: int, adj: List[List[List[int]]]) -> int:
        edges = []
        for i in range(V):
            for it in adj[i]:
                adjNode, wt = it
                node = i
                edges.append((wt, (node, adjNode)))

        ds = DisjointSet(V)
        print("adj:",adj)
        print(edges)
        edges.sort()
        mstWt = 0
        for wt, (u, v) in edges:
            if ds.findUPar(u) != ds.findUPar(v):
                mstWt += wt
                ds.unionBySize(u, v)
        print(edges)
        return mstWt

V = 5
edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]]
adj = [[] for _ in range(V)]
for it in edges:
    adj[it[0]].append((it[1], it[2]))
    adj[it[1]].append((it[0], it[2]))

obj = Solution()
mstWt = obj.spanningTree(V, adj)
print("The sum of all the edge weights:", mstWt)
