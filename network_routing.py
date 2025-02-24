import math
from Data_Structures import pop_min, PriorityHeap


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
    print(
        f"find_shortest_path_with_array({graph}, {source}, {target})")  # TODO: remove this line after you implement this functionsource, target)
    nodes = set()
    for parent, edges in graph.items():
        nodes.add(parent)
        nodes.update(edges.keys())
    print(f"nodes = {nodes}")
    dist = {}
    prev = {}
    for node in nodes:
        dist[node] = math.inf
        prev[node] = None

    dist[source] = 0
    H = PriorityHeap()
    H.Insert(source, 0)

    while H:
        u = H.delete_min()
        parent = u[0]
        for v, w in graph[parent].items():
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                H.Insert(v, dist[v])

    path = [target]
    while target != source:
        target = prev[target]
        path.append(target)

    path.reverse()
    return path, dist[target]






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
    nodes = set()
    for parent, edges in graph.items():
        nodes.add(parent)
        nodes.update(edges.keys())
    print(f"nodes = {nodes}")
    dist = {}
    prev = {}
    for node in nodes:
        dist[node] = math.inf
        prev[node] = None

    dist[source] = 0

    H = {source: 0}
    while H:
        u = pop_min(H)
        for v, w in graph[u[0]].items():
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                H[v] = dist[v]



    total_weight = dist[target]
    path = []
    current = target
    while current != source:
        current = prev[current]
        path.append(current)
    path.append(source)
    path.reverse()



    return path, total_weight