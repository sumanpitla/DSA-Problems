from queue import PriorityQueue

class Solution:
    def spanningTree(self, V, adj):
        pq = PriorityQueue()
        vis = [0] * V
        pq.put((0, 0))
        sum = 0

        while not pq.empty():
            wt, node = pq.get()
            if vis[node] == 1:
                continue

            vis[node] = 1
            sum += wt

            for adjNode, edW in adj[node]:
                if not vis[adjNode]:
                    pq.put((edW, adjNode))

        return sum

V = 5
edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]]
adj = [[] for _ in range(V)]
for it in edges:
    adj[it[0]].append((it[1], it[2]))
    adj[it[1]].append((it[0], it[2]))

obj = Solution()
sum = obj.spanningTree(V, adj)
print("The sum of all the edge weights:", sum)
