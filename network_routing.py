import math
from Data_Structures import pop_min


def find_shortest_path_with_heap(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the heap-based algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """




def find_shortest_path_with_array(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the array-based (linear lookup) algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """
    print(f"find_shortest_path_with_array({graph}, {source}, {target})")  # TODO: remove this line after you implement this functionsource, target)
    nodes = {}
    for parent, edges in graph.items():
        nodes.add(parent)
        nodes.update(edges.keys())
    print(f"nodes = {nodes}")  # TODO: remove this line after you implement this function (list of nodes)
    dist = {}
    prev = {}
    for node in nodes:
        dist[node] = math.inf
        prev[node] = None

    dist[source] = 0
     # TODO: implement this function

    H = {source: 0}
    while H:
        u = pop_min(H)
        for v, w in graph[u].items():
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                H.append(v)
    return []