


def pop_min(H: dict[int, float]) -> tuple[int, float]:
    smallest = float('inf')
    node = None

    for key,weight in H.items():
        if weight < smallest:
            smallest = weight
            node = key
    del H[node]

    return node