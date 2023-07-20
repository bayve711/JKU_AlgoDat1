class MaxHeap:
    def __init__(self, input_array):
        """
        @param input_array from which the heap should be created
        @raises ValueError if list is None.
        Creates a bottom-up max heap in place.
        """
        self.heap = None
        self.size = 0
        if input_array is None:
            raise ValueError
        else:
            self.heap = input_array
            self.size = len(input_array)
            self.non_leaf = self.size // 2 - 1
            for i in range(self.non_leaf, -1, -1):
                parent = i
                while True:
                    left_child = 2 * parent + 1
                    right_child = 2 * parent + 2
                    max_child = parent

                    if left_child < self.size and self.heap[left_child] > self.heap[max_child]:
                        max_child = left_child
                    if right_child < self.size and self.heap[right_child] > self.heap[max_child]:
                        max_child = right_child

                    if max_child == parent:
                        break

                    self.heap[parent], self.heap[max_child] = self.heap[max_child], self.heap[parent]
                    parent = max_child


    def get_heap(self):
        # helper function for testing, do not change
        return self.heap

    def get_size(self):
        """
        @return size of the max heap
        """
        return self.size

    def contains(self, val):
        """
        @param val to check if it is contained in the max heap
        @return True if val is contained in the heap else False
        @raises ValueError if val is None.
        Tests if an item (val) is contained in the heap. Does not search the entire array sequentially, but uses the
        properties of a heap.
        """
        if val is None:
            raise ValueError
        elif self.heap is None:
            return False
        else:
            left_bound = 0
            right_bound = len(self.heap) - 1

            while left_bound <= right_bound:
                mid = (left_bound + right_bound) // 2
                if self.heap[mid] == val:
                    return True
                elif self.heap[mid] < val:
                    left_bound = mid + 1
                else:
                    right_bound = mid - 1
            return False

    def sort(self):
        """
        This method sorts (ascending) the list in-place using HeapSort, e.g. [1,3,5,7,8,9]
        """

        for i in range(self.size - 1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.size -= 1
            self.down_heap(0)

    def remove_max(self):
        """
        Removes and returns the maximum element of the heap
        @return maximum element of the heap or None if heap is empty
        """
        if self.size == 0:
            return None
        else:
            maximum = self.heap[0]
            self.heap[0] = self.heap[self.size - 1]
            self.heap.pop()
            self.size -= 1
            self.down_heap(0)
            return maximum


    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return (2 * index) + 1

    def right_child(self, index):
        return (2 * index) + 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def down_heap(self, i):
        left_child = self.left_child(i)
        right_child = self.right_child(i)
        cur = i

        if left_child < self.size and self.heap[left_child] > self.heap[cur]:
            cur = left_child

        if right_child < self.size and self.heap[right_child] > self.heap[cur]:
            cur = right_child

        if cur != i:
            self.heap[i], self.heap[cur] = self.heap[cur], self.heap[i]
            self.down_heap(cur)
