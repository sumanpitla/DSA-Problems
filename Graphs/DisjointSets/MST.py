#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        pq = []
        #heapq.heapify(pq)

        vis = [0] * V
        heapq.heappush(pq, (0, 0))
        sum = 0

        while pq:
            wt, node = heapq.heappop(pq)

            if vis[node] == 1:
                continue

            vis[node] = 1
            sum += wt

            for it in adj[node]:
                adjNode, edW = it[0], it[1]
                if not vis[adjNode]:
                    heapq.heappush(pq, (edW, adjNode))

        return sum
        """
        print(adj)
        pq=[]
        pq.append((0,0))
        vis=[0]*(V)
        sumi=0
        while pq:
            wt,node=heapq.heappop(pq)
            if  vis[node]==1:
                continue
            vis[node]=1
            sumi+=wt
            for edw, adjnode in adj[node]:
                if not vis[adjnode]:
                    heapq.heappush(pq,(edw,adjnode))
        return sumi
        """
                    
        #code here

