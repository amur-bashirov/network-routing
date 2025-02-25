# test_priority_heap.py
import unittest
from queue_structures import PriorityHeap

class TestPriorityHeap(unittest.TestCase):

    def is_min_heap(heap):
        n = len(heap)
        for i in range(n):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and heap[i][1] > heap[left][1]:
                return False
            if right < n and heap[i][1] > heap[right][1]:
                return False
        return True
    def setUp(self):
        self.pq = PriorityHeap()

    def test_insert_and_delete_min(self):
        self.pq.insert(1, 5)
        self.pq.insert(2, 3)
        self.pq.insert(3, 9)
        self.assertEqual(self.pq.delete_min(), (2, 3))
        self.assertEqual(self.pq.delete_min(), (1, 5))
        self.assertEqual(self.pq.delete_min(), (3, 9))
        with self.assertRaises(IndexError):
            self.pq.delete_min()

    def test_insert_existing_node(self):
        self.pq.insert(2, 3)
        self.pq.insert(2, 1)  # Assuming your heap allows updating existing nodes
        self.assertEqual(self.pq.delete_min(), (2, 1))

    def test_large_input(self):
        import random
        nodes = list(range(100))
        distances = random.sample(range(1, 1001), 100)
        for node, distance in zip(nodes, distances):
            self.pq.insert(node, distance)
        boolean = TestPriorityHeap.is_min_heap(self.pq.H)
        self.assertTrue(boolean)
        print(f"{self.pq.H}")
        sorted_distances = sorted(distances)
        for expected_distance in sorted_distances:
            node, actual_distance = self.pq.delete_min()
            self.assertEqual(actual_distance, expected_distance)

    def test_decrease_key(self):
        self.pq.insert(1, 50)
        self.pq.insert(2, 30)
        self.pq.insert(3, 40)
        self.pq.insert(4, 60)

        # Decrease key of node 3 from 40 to 20
        self.pq.decrease_key(3, 20)

        # Ensure min-heap property is maintained
        boolean = TestPriorityHeap.is_min_heap(self.pq.H)
        self.assertTrue(boolean)

        # Ensure the order of deletion is now correct
        self.assertEqual(self.pq.delete_min(), (3, 20))
        self.assertEqual(self.pq.delete_min(), (2, 30))
        self.assertEqual(self.pq.delete_min(), (1, 50))
        self.assertEqual(self.pq.delete_min(), (4, 60))

        # Ensure error is raised when decreasing key to a higher value
        self.pq.insert(5, 25)
        with self.assertRaises(ValueError):
            self.pq.decrease_key(5, 35)  # Trying to increase the key instead

        # Ensure error is raised when trying to decrease a key for a non-existent node
        with self.assertRaises(KeyError):
            self.pq.decrease_key(10, 5)  # Node 10 doesn't exist


if __name__ == '__main__':
    unittest.main()

