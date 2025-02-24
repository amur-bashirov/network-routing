


def pop_min(H: dict[int, float]) -> tuple[int, float]:
    smallest = float('inf')
    node = None

    for key,weight in H.items():
        if weight < smallest:
            smallest = weight
            node = key
    del H[node]

    return node


class PriorityHeap:
    def __init__(self):
        self.H = []



    def Insert(self, node: int, distance: float):
        new_tuple = (node,distance)
        self.H.append((node,distance))
        self.bubble_up(node, distance)



    def bubble_up(self, node: int, distance: float):
        pass


    def bubble_down(self, node: int, distance: float):
        pass




    def delete_min(self) -> tuple[int, float]:
        pass