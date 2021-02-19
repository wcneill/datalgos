# undirected graph class
class Undirected:
    def __init__(self, edges):
        """
        Instantiate an undirected graph.

        :param edges: list of tuples representing a single edge between two nodes (node1, node2, weight)
        """

        # graph[node][neighbor][weight]
        self.edges = edges
        self.graph = {}

        for edge in edges:

            if edge[0] not in self.graph:
                self.graph[edge[0]] = {edge[1]: edge[2]}
            else:
                self.graph[edge[0]][edge[1]] = edge[2]

            if edge[1] not in self.graph:
                self.graph[edge[1]] = {edge[0]: edge[2]}
            else:
                self.graph[edge[1]][edge[0]] = edge[2]

    def __str__(self):
        return self.graph.__str__()

    def __getitem__(self, key):
        return self.graph[key]

    def __setitem__(self, key, value):
        self.graph[key] = value











