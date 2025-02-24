


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
        self.H.append((node,distance))
        index = len(self.H)
        self.bubble_up(node, distance, index)


    def delete_min(self) -> tuple[int, float]:
        root = self.H[0]
        self.H[0] = self.H[-1]
        del self.H[-1]
        self.bubble_down(root[0], root[1])
        return root



    def bubble_up(self, node: int, distance: float, index: int):
        if index == 0:
            return
        updated = False
        while not updated:
            if index == 1:
                return
            parent_index = index // 2
            if distance < self.H[parent_index-1][1]:
                updated = True
                self.H[index-1] = self.H[parent_index-1]
                self.H[parent_index-1] = (node, distance)
                index = parent_index
            else:
                return


    def bubble_down(self, node: int, distance: float):
        #pay attention to index and node, they are different. Change that.
        index = 0
        updated = False
        while not updated:
            child1 = 2 * node
            child2 = 2 * node + 1
            if child1 > len(self.H) or child2 > len(self.H):
                return
            smallest = ()
            biggest = ()
            if self.H[child1][1] < self.H[child2][1]:
                smallest = self.H[child1]
                biggest = self.H[child2]
            else:
                smallest = self.H[child2]
                biggest = self.H[child1]
            if distance > smallest[1]:
                updated = True
                self.H[node] = smallest
                self.H[smallest[0]] = (node, distance)
                node = smallest[0]
            elif distance > biggest[1]:
                return
