# Python program for Bellman-Ford's 
# single source shortest path algorithm

# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices #No. of vertices
        self.graph = []

    # Function to add edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # Utility function used to print the solution
    def printArr(self, dist):
        print("Vertex distance from source: ")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    # Main function hat finds the shortest distances from source 
    # to all other vertices using Bellman Ford Algorithm. 
    # The function also detects neqative weight cycle
    def BellmanFord(self, src):

        # Step 1: Initialize distances from src to all other vertices 
        dist = [float("inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 lines. A simple
        # shortest path from src to any other vertices can 
        # have at most |V| - 1 lines
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of 
            # the picked vertex. Consider only those vertices which are still in queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: check for negative weight cycles. the above step
        # guarantees shortest distances if graph doesn't contain
        # negative wieght cycles. if we get a shorter path, then there is a cycle

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("The graph contains newgative weight cycle.")
                return
            
        # Print all distances
        self.printArr(dist)

# Driver code
if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 3)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)

    # Function call
    g.BellmanFord(0)
    
