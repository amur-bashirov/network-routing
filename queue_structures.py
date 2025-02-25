


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
        self.H = [None]
        self.position_map = {}

    def __len__(self):
        return len(self.H) -1



    def insert(self, node: int, distance: float):
        self.H.append((node,distance))
        index = len(self.H)-1
        self.position_map[node] = index
        self.bubble_up(node, distance, index)


    def delete_min(self) -> tuple[int, float]:
        if len(self.H) <= 1:
            raise IndexError("delete_min() called on empty heap")


        root = self.H[1]
        removed = self.position_map.pop(root[0])
        self.H[1] = self.H[-1]

        if len(self.H) > 2:
            self.position_map[self.H[1][0]] = 1
        del self.H[-1]


        if len(self.H) > 1:
            self.bubble_down(self.H[1][0], self.H[1][1])
        return root

    def decrease_key(self, node: int, new_distance: float):
        """Decrease the priority of a node and restore heap order."""

        if node not in self.position_map:
            self.insert(node, new_distance)
            return
        index = self.position_map[node]


        self.H[index] = (node, new_distance)
        self.bubble_up(node, new_distance, index)

    def bubble_up(self, node: int, distance: float, index: int):


        while True:

            if index == 1:
                return
            parent_index = index // 2

            parent = self.H[parent_index]
            if distance < parent[1]:
                self.position_map[parent[0]] = index
                self.H[index] = self.H[parent_index]
                self.H[parent_index] = (node, distance)
                self.position_map[node] = parent_index
                index = parent_index
            else:
                return


    def bubble_down(self, node: int, distance: float):
        #pay attention to index and node, they are different. Change that.
        index = 1
        n = len(self.H) - 1
        while True:
            child1 = 2 * index
            child2 = 2 * index + 1


            smallest = 0
            if child1 > len(self.H)-1:
                return
            if child2 >len(self.H)-1:
                smallest = child1
            elif self.H[child1][1] < self.H[child2][1]:
                smallest = child1
            else:
                smallest = child2



            if self.H[smallest][1] < distance:

                self.position_map[self.H[smallest][0]] = index
                self.H[index] = self.H[smallest]
                self.H[smallest] = (node, distance)
                self.position_map[node] = smallest
                index = smallest
            else:
                return
