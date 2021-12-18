class Graph:
    class _Vertex:

        def __init__(self, value = None):
            self.value = value

        def __str__(self) -> str:
            return f'{self.value}'

        def __repr__(self) -> str:
            return f'{self.value}'

        def __hash__(self):
            return hash(id(self))

        def __eq__(self, k):
            return self.value == k.value

    class _Edge:

        def __init__(self, u, v):
            self._origin = u
            self._destination = v

        def get_endpoints(self):
            return self._origin, self._destination

        def get_destination(self):
            return self._destination

        def get_opposite(self, v):
            # return the destination if v is origin, if destination, return the origin.
            return self._destination if v is self._origin else self._origin

        def __str__(self) -> str:
            return f'{self._origin} -> {self._destination} '

        def __repr__(self) -> str:
            return f'{self._origin} -> {self._destination} '

        def __hash__(self):
            # print(hash(str(self)))
            return hash( (self._origin, self._destination ))

    def __init__(self):
        self.vertices = {}
        self.outgoing = {}
        self.incoming = {}

    def __str__(self) -> str:
            return f'{self.outgoing} : {self.incoming}'

    def __repr__(self) -> str:
        return f'{self.outgoing} : {self.incoming}'
    
    def get_vertices(self):
        return self.vertices.keys()
    
    # def get_vertices_value(self):
    #     return [x.value for x in self.vertices.keys()]

    def get_vertex(self, v):
        return self.vertices[v]

    def add_vertex(self, element):        
        
        if element in self.get_vertices():
            return self.vertices[element]
        else:
            vertex = self._Vertex(element)
            self.vertices[element] = vertex
            self.outgoing[vertex] = {}
            self.incoming[vertex] = {}
            return vertex

    def add_edge(self, u, v):
        if u.value != v.value: #exclude edges that move to themselves
            edge = self._Edge(u,v)
            self.outgoing[u][v] = edge
            self.incoming[v][u] = edge

    def get_edge(self, u, v):
        return self.outgoing[u].get(v)

    def get_outgoing(self, u):

        for edge in self.outgoing[u].values():
            yield edge

    def get_incoming(self, u):

        for edge in self.incoming[u].values():
            yield edge
        
    def edges(self):
        result = set()
        for secondary_map in self.outgoing.values():
            result.update(secondary_map.values())
        return result


    def dijkstra_algo(self, src):
        '''
        src: takes a vertex class and is the starting vertex. 
        returns: cloud, d
        '''
        d = {}
        cloud = {} # Returns how many nodes it takes to get to that location.  for example 1: 2 means it takes 2 nodes to get from 0 to 1.
        pq = {} #using a dict as a queue to get it working. 
        pqlocator = {}

        # for each instance of vertex v add an entry to the priority queue, with
        # the source having distance 0 and all others having infinite distance. 
        for v in self.get_vertices():
            v = self.get_vertex(v)

            if v is src: 
                d[v] = 0
            else:
                d[v] = float('inf')
            
            pq[v] = d[v]
            # pqlocator[v] = v

        while len(pq) > 0 : # mod for list 
        #     key, u = pq.remove_min() #### need to change this for our implementation. 
            u = min(pq, key=pq.get) # this will grab the initial src node. 
            
            cloud[u] = pq[u] #setting this to min value for traversal for src its 0

            del pq[u]

            for e in self.get_outgoing(u): #this is a generator function.

                v = e.get_opposite(u) 

                if v not in cloud:
                    wgt = 1  # I did not emplement an element value in the edge class, thus jsut using 1.
                    if d[u] + wgt < d[v]:
                        d[v] = d[u] + wgt 
                        pq[v] = d[v] 
                        
        return cloud, d

    def get_equidistant_node_count(self, starting_vertex, second_vertex):

        cloud_0, d_0 = self.dijkstra_algo(starting_vertex)
        cloud_1, d_1 = self.dijkstra_algo(second_vertex)

        count= 0
        for x in cloud_0.keys():
            if cloud_0[x] == cloud_1[x]:
                count += 1
        return count

    def shortest_path_tree(self, src):
        cloud, d = self.dijkstra_algo(src)

        tree={}
        for v in d:
            if v is not src:
                for e in self.get_incoming(v):
                    u = e.get_opposite(v)
                    wgt = 1
                    if d[v] == d[u] + wgt:
                        tree[v] = e
        return tree

        #tree_paths = shortest_path_tree(new_graph, new_graph.get_vertex(0),d_0)

    def get_best_path(self, start, end):

        tree = self.shortest_path_tree(start)

        path = {}

        count = 0

        path[count] = tree[end]

        while tree[end]._origin != start:

            count += 1
            path[count] = tree[tree[end]._origin]
            end = tree[end]._origin

        new_order = [x for x in path.keys()]
        new_order.reverse()

        steps_in_order = [ path[x] for x in new_order]

        return steps_in_order

# Open file.
with open('adj.txt') as f:
    contents = f.readlines()

#clean file contents
matrix = []
for line in contents:
    line = line.replace('  \n', '')
    line = line.split(' ')
    line = [int(x) for x in line]
    matrix.append(line)

# Open file.
with open('input.txt') as f:
    contents = f.readlines()
 
input_nodes = []
for line in contents:
    line = line.replace('  \n', '')
    line = line.split(' ')
    line = [int(x) for x in line]
    input_nodes.append(line)


#populate the graph
new_graph = Graph()
for row in range(len(matrix)):
    current_vertex = new_graph.add_vertex(row)

    for column in range(len(matrix[row])): 
        to_vertex = new_graph.add_vertex(column)
            
        if matrix[row][column] == 1:
            new_graph.add_edge(current_vertex, to_vertex ) 


#Loop through lines and solve.
result = []
for line in input_nodes:
    number_equidistant_nodes = new_graph.get_equidistant_node_count(new_graph.get_vertex(line[0]), new_graph.get_vertex(line[1]))
    result.append(number_equidistant_nodes)

#output values to an ouput file.
output = open("output.txt", "w")
lines = output.writelines( [str(x) + "\n" for x in result])
output.close()












