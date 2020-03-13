#!/usr/bin/env python3

import re
import itertools

ROLLNUM_REGEX = "201[0-9]{4}"

class Graph(object):
    name = "Ira Aggarwal"
    email = "ira18039@iiitd.ac.in"
    roll_num = "2018039"


    def __init__ (self, vertices, edges):
        """
        Initializes object for the class Graph

        Args:
            vertices: List of integers specifying vertices in graph
            edges: List of 2-tuples specifying edges in graph
        """

        self.vertices = vertices
        
        ordered_edges = list(map(lambda x: (min(x), max(x)), edges))
        
        self.edges    = ordered_edges

        self.all_paths_list = []
        
        self.validate()

    def validate(self):
        """
        Validates if Graph if valid or not

        Raises:
            Exception if:
                - Name is empty or not a string
                - Email is empty or not a string
                - Roll Number is not in correct format
                - vertices contains duplicates
                - edges contain duplicates
                - any endpoint of an edge is not in vertices
        """

        if (not isinstance(self.name, str)) or self.name == "":
            raise Exception("Name can't be empty")

        if (not isinstance(self.email, str)) or self.email == "":
            raise Exception("Email can't be empty")

        if (not isinstance(self.roll_num, str)) or (not re.match(ROLLNUM_REGEX, self.roll_num)):
            raise Exception("Invalid roll number, roll number must be a string of form 201XXXX. Provided roll number: {}".format(self.roll_num))

        if not all([isinstance(node, int) for node in self.vertices]):
            raise Exception("All vertices should be integers")

        elif len(self.vertices) != len(set(self.vertices)):
            duplicate_vertices = set([node for node in self.vertices if self.vertices.count(node) > 1])

            raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(vertices, duplicate_vertices))

        edge_vertices = list(set(itertools.chain(*self.edges)))

        if not all([node in self.vertices for node in edge_vertices]):
            raise Exception("All endpoints of edges must belong in vertices")

        if len(self.edges) != len(set(self.edges)):
            duplicate_edges = set([edge for edge in self.edges if self.edges.count(edge) > 1])

            raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(edges, duplicate_edges))

    def min_dist(self, start_node, end_node):
        '''
        Finds minimum distance between start_node and end_node

        Args:
            start_node: Vertex to find distance from
            end_node: Vertex to find distance to

        Returns:
            An integer denoting minimum distance between start_node
            and end_node
        '''
        visited = [] # list of visited nodes
        current_level = [] # current level list with current level node
        current_level.append(start_node)
        next_level = [] # nodes on next level
        distance = 1
        visited.append(tuple((start_node, 0)))
        while current_level:
            for element in current_level:
                for edgeElement in edges: # matching with tuple in edges
                    if element in edgeElement: 
                        neighbor = edgeElement[0] if element==edgeElement[1] else edgeElement[1] # the other element in edges is the neighbor
                        flag = False 
                        for elt in visited:
                            if neighbor == elt[0]:
                                flag = True # if neighbor is in the visited list
                                break
                        if not flag:
                            next_level.append(neighbor) # if neighbor is not in visited list append in next level
                            visited.append(tuple((neighbor, distance)))
            distance += 1 # distance from start node
            current_level = next_level # current level becomes equal to the next level
            next_level = []
        endNode_distance = []
        for element in visited:
            if element[0] == end_node: # finding distance of end node from start node
                endNode_distance.append(element[1]) 
        minDistance = min(endNode_distance) # finding minimum distance
        return minDistance

        raise NotImplementedError

    def all_paths(self, node, destination, dist, path):
        """
        Finds all paths from node to destination with length = dist

        Args:
            node: Node to find path from
            destination: Node to reach
            dist: Allowed distance of path
            path: path already traversed

        Returns:
            List of path, where each path is list ending on destination. Length of list = dist

            Returns None if there no paths
        """
        final_list = []
        self.all_paths_list = [] 
        self.path_src_dest(node, destination, dist, path) # list of all possible paths between start and end node
        for element in self.all_paths_list:
            if len(element) == dist + 1:
                final_list.append(element) # finding paths with length = distance
        return final_list

    def path_src_dest(self, node, destination, dist, path):
        """
        Finds all paths between node and destination. The paths can be of any length.

        Args:
            node: Node to find path from
            destination: Node to reach
            dist: Allowed distance of path
            path: path already traversed

        Returns:
            List of path, where each path is list ending on destination

            Returns None if there no paths
        """

        if node == destination:
            self.all_paths_list.append((path+[node])) # if node is equal to destination return the path after adding node to it
        else:
            for edgeElement in edges:
                if node in edgeElement:
                    neighbor = edgeElement[0] if node == edgeElement[1] else edgeElement[1] # finding neighbor of node
                    if neighbor not in path:
                        self.path_src_dest(neighbor, destination, dist, path+[node]) # if neghbor is not in path function is recursively called again


    def all_shortest_paths(self, start_node, end_node):
        """
        Finds all shortest paths between start_node and end_node

        Args:
            start_node: Starting node for paths
            end_node: Destination node for paths

        Returns:
            A list of path, where each path is a list of integers.
        """
        dist = self.min_dist(start_node, end_node) # min distance between start and end node
        pathList = self.all_paths(start_node, end_node, dist, []) # list of all paths with shortest distance between start and end node
        return pathList

        raise NotImplementedError


    def betweenness_centrality(self, node):
        """
        Find betweenness centrality of the given node

        Args:
            node: Node to find betweenness centrality of.

        Returns:
            Single floating point number, denoting betweenness centrality
            of the given node
        """
        betweennessCentrality = 0
        pair_List = []
        for i in range(0, len(vertices)-1):
            for j in range(i+1, len(vertices)):
                pair_List.append(tuple((vertices[i], vertices[j]))) # all possible pair of vertices
        pairList = []
        for pair in pair_List:
            if node not in pair:
                pairList.append(pair) # all possile pair of vertices excluding the node
        for pair in pairList:
            paths = self.all_shortest_paths(pair[0], pair[1])
            x = len(paths) # no. of shortest possible paths 
            yList = [] 
            for element in paths:
                if node in element:
                    yList.append(element)
            y = len(yList) # no. of shortest possible paths passing through the node
            betweennessCentrality += y/x
        return betweennessCentrality


        raise NotImplementedError

    def top_k_betweenness_centrality(self):
        """
        Find top k nodes based on highest equal betweenness centrality.

        
        Returns:
            List a integer, denoting top k nodes based on betweenness
            centrality.
        """
        bc_list = [] # list of tuples with node and standardised betweenness centrality
        bc_value = [] # list of standardised betweenness centralities
        n = len(vertices)
        divide = (n-1)*(n-2) / 2
        for node in vertices:
            standardized_betweenness_centrality = self.betweenness_centrality(node)/divide # standardised
            bc_list.append(tuple((standardized_betweenness_centrality, node)))
        maxNode = []
        bc_list.sort(reverse = True) # decreasing order in list
        for element in bc_list:
            bc_value.append(element[0])
        max_bc = max(bc_value) # finding maximum standard betweenness centrality
        for element in bc_list:
            if element[0] == max_bc:
                maxNode.append(element[1]) # finding all nodes with this value of standard betweenness centrality
        return maxNode # list of nodes returned

        raise NotImplementedError

if __name__ == "__main__":
    vertices = [1, 2, 3, 4, 5, 6]
    edges    = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)]

    graph = Graph(vertices, edges)
    print(graph.top_k_betweenness_centrality())