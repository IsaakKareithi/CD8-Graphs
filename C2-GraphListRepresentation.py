# A python program to demonstrate the adjacency
# list representation of the graph 

# A Class to represent the adjacency list of the node
class adjNode:
    def __init__(self, data):
        self.vertex = data 
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding a node to the source node
        node = adjNode(src)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination
        # since it is the undirected graph
        node = adjNode(src)
        node.next = self.graph(dest)
        self.graph[dest] = node

    # Function to print the graph 
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head.".format(i), end=' ')
            temp = self.graph[i]
            while temp:
                print('--> {}'.format(temp.vertex), end=' ')

            print('  \n')
            