from collections import defaultdict

# Class to build the graph
class Graph():
    def __init__(self):
        # self.edges is a dict of all possible next nodes
        self.edges = defaultdict(list)
        # self.weights has all the weights between two nodes
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # build undirected weighted graph
        # Creating the undirected graph as adjacency list
        self.edges[from_node].append(to_node) 
        self.edges[to_node].append(from_node)
        # Creating the list of all weights with 
        # key as two connecting nodes (tuple) and 
        # value as respective weight
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

graph = Graph()

# PARAMS
# n: number of nodes in the graph
# edges: 2D array of integers where each edge has 
# start and end nodes of an edge, followed by its length
# s: start node number
def shortestReach(n, edges, s):
    # loop to iterate over every edge of the graph
    for edge in edges:
        graph.add_edge(*edge)

    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {s: (None, 0)}
    current_node = s # start from source node
    end_node = n 
    visited = set() # track visited nodes

    # loop until all nodes are visited
    while current_node != end_node: 
        visited.add(current_node) # update visited
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1] 

        # iterate all possible next nodes
        for next_node in destinations:
            # get total weight to visit next node
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                # update next node with current node and weight
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                # check if weight is lower 
                if weight < current_shortest_weight:
                    # update shortest weight if true
                    shortest_paths[next_node] = (current_node, weight)
            # dict of dict of all possible paths
            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Oops! Connecting path doesn't exist :("

        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []       
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node

    # return an array of integers representing shortest distance 
    # to each node from start node in ascending order
    path = path[::-1]      
    return path

# Input Format
# The first line contains t, the number of test cases.
t = int(input('\nPlease input the number of test cases: '))
while t < 1 or t > 10:
     t = int(input('Wrong input! Test cases should be between 1 and 10: '))

# Each test case is as follows:
for j in range(t):
    print('\nTest Case '+str(j+1)+':')
    # - The first line contains two space-separated integers n and m, the number of nodes and edges in the graph.
    n = int(input('\nPlease input the number of nodes in the graph: '))
    while n < 2 or n > 3000:
        n = int(input('Wrong input! Nodes should be between 2 and 3000: '))

    m = int(input('Please input the number of edges in the graph: '))
    max_edges = n*((n - 1)/2)
    while m < 1 or m > max_edges:
        m = int(input('Wrong input! Edges should be between 1 and ' + str(max_edges)+' : '))

    # - Each of the next m lines contains three space-separated integers x, y, and r, the beginning and ending nodes of an edge, and the length of the edge.
    edges = []
    nodes = set()
    for i in range(m):
        x = int(input('\nPlease input the start node of edge '+str(i+1)+' : '))
        while x < 1:
            x = int(input('Wrong input! Start node should be a natural number: '))
        nodes.add(x)

        y = int(input('Please input the end node of edge '+str(i+1)+' : '))
        while y < 1:
            y = int(input('Wrong input! End node should be a natural number: '))
        nodes.add(y)

        r = int(input('Please input the length of edge '+str(i+1)+' : '))
        while r < 1 or r > 10**5:
            r = int(input('Wrong input! Length should be between 1 and 100000: '))

        # 2D array of integers (edges) where each edge has 
        # start and end nodes of an edge, 
        # followed by its length
        edge = [x,y,r]
        edges.append(edge)

    # - The last line of each test case has an integer s, denoting the starting position.
    s = int(input('\nPlease input the source node of the graph: '))
    while s not in nodes:
        s = int(input('Wrong input! Start node should be in the graph: '))

    # print a single line consisting of n - 1 space-separated integers 
    # denoting the shortest distance to the n - 1 nodes 
    # from starting position s in increasing order of their labels
    print('\n')
    path = shortestReach(len(nodes), edges, s)
    path.pop(0) # excluding s
    print('Shortest path:', *path, sep=' ')

    # Add nodes with no routes, with the distance (-1)
    if n > m:
        v = set()
        for i in range(n):
            v.add(i+1)
        # nodes with no routes
        d = v.difference(nodes) 
        for i in range(len(d)):
            path.append(-1) 
        print('Shortest path (no routes inclusive):', *path, sep=' ')
    print('\n')