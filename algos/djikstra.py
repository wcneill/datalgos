import random
import timeit
from dstructs import graphs


def djikstra(graph, start, end):

    current_node = start
    shortest_path = {start: (start, 0)}
    visited = []

    while current_node != end:
        visited.append(current_node)
        neighbors = graph[current_node]

        for neighbor in neighbors:

            edge_weight = graph[current_node][neighbor]
            cum_weight = shortest_path[current_node][1] + edge_weight

            if neighbor not in shortest_path:
                shortest_path[neighbor] = (current_node, cum_weight)
            elif shortest_path[neighbor][1] > cum_weight:
                shortest_path[neighbor] = (current_node, cum_weight)

        next_nodes = [node for node in shortest_path if node not in visited]
        try:
            current_node = random.choice(next_nodes)
            ## Surprisingly, the below is slower, perhaps because of the lambda key?
            # current_node = min(next_nodes, key=lambda i: shortest_path[i][1])
        except IndexError:
            return "Path not possible"

    current_node = end
    final_path = []
    while current_node != start:
        cum_weight = shortest_path[current_node][1]
        final_path.append((current_node, cum_weight))
        current_node = shortest_path[current_node][0]
    final_path.append((start, 0))
    final_path.reverse()
    return final_path


if __name__ == '__main__':
    edges = [
        ('X', 'A', 7),
        ('X', 'B', 2),
        ('X', 'C', 3),
        ('X', 'E', 4),
        ('A', 'B', 3),
        ('A', 'D', 4),
        ('B', 'D', 4),
        ('B', 'H', 5),
        ('C', 'L', 2),
        ('D', 'F', 1),
        ('F', 'H', 3),
        ('G', 'H', 2),
        ('G', 'Y', 2),
        ('I', 'J', 6),
        ('I', 'K', 4),
        ('I', 'L', 4),
        ('J', 'L', 1),
        ('K', 'Y', 5),
    ]

    graph = graphs.Undirected(edges)
    shortest = djikstra(graph, 'X', 'Y')

    print(f'shortest path: {shortest}')
    print(timeit.timeit(lambda: djikstra(graph, 'X', 'Y'), number=10000))