from my_list_node import MyListNode


class MySortedDoublyLinkedList:
    """A base class providing a doubly linked list representation."""

    def __init__(self, head: 'MyListNode' = None, tail: 'MyListNode' = None, size: int = 0) -> None:
        """Create a list and default values are None."""
        self._head = head
        self._tail = tail
        self._size = size

    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    def __str__(self) -> str:
        """Return linked list in string representation."""
        result = []
        node = self._head
        while node:
            result.append(node.elem)
            node = node.next_node
        return str(result)

    # The following methods have to be implemented.

    def get_value(self, index: int) -> int:
        """Return the value (elem) at position 'index' without removing the node.

        Args:
            index (int): 0 <= index < length of list

        Returns:
            (int): Retrieved value.

        Raises:
            ValueError: If the passed index is not an int or out of range.
        """
        try:
            if not isinstance(index, int) or index < 0 or index > self._size - 1:
                raise ValueError
            if index >= 0 and index < self._size:
                node = self._head
                for i in range(self._size):
                    if i == index:
                        return node.elem
                    else:
                        node = node.next_node
            else:
                raise ValueError
        except:
            raise ValueError

    def search_value(self, val: int) -> int:
        """Return the index of the first occurrence of 'val' in the list.

        Args:
            val (int): Value to be searched.

        Returns:
            (int): Retrieved index.

        Raises:
            ValueError: If val is not an int.
        """
        try:
            node = self._head
            for i in range(self._size):
                if int(val) == node.elem:
                    return i
                else:
                    node = node.next_node
            return -1
        except:
            raise ValueError

    def insert(self, val: int) -> None:
        """Add a new node containing 'val' to the list, keeping the list in ascending order.

        Args:
            val (int): Value to be added.

        Raises:
            ValueError: If val is not an int.
        """

        if not isinstance(val, int):
            raise ValueError
        try:
            node = MyListNode(val)

            if self._size == 0:
                self._head = node
                self._tail = node
            elif val < self._head.elem:
                self._head.prev_node = node
                node.next_node = self._head
                self._head = node
            elif val > self._tail.elem:
                self._tail.next_node = node
                node.prev_node = self._tail
                self._tail = node
            else:
                cur = self._head
                while cur.next_node.elem <= val:
                    cur = cur.next_node
                node.prev_node = cur
                node.next_node = cur.next_node
                cur.next_node.prev_node = node
                cur.next_node = node

            self._size += 1

        except:
            raise ValueError

    def remove_first(self, val: int) -> bool:
        """Remove the first occurrence of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether an element was successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError
        try:
            i = self.search_value(val)
            val = self.get_value(i)
            cur = self._head
            if self._size == 0:
                return False
            for n in range(self._size):
                if n != i:
                    cur = cur.next_node
                else:
                    if val == self._head.elem:
                        cur.next_node.prev_node = None
                        cur.next_node = None
                        cur.elem = None
                        self._size -= 1
                        return True
                    elif val == self._tail.elem:
                        cur.prev_node.next_node = None
                        cur.prev_node = None
                        cur.elem = None
                        self._size -= 1
                        return True
                    else:
                        cur.prev_node.next_node = cur.next_node
                        cur.next_node.prev_node = cur.prev_node
                        cur.prev_node = None
                        cur.next_node = None
                        cur.elem = None
                        self._size -= 1
                        return True
        except:
            raise ValueError



    def remove_all(self, val: int) -> bool:
        """Remove all occurrences of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether elements were successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError
        try:
            i = self.search_value(val)
            val = self.get_value(i)
            if self._size == 0:
                return False
            cur = self._head
            for n in range(self._size):
                if n != i:
                    cur = cur.next_node
                else:
                    if val == self._head.elem:
                        temp = cur.next_node
                        temp.prev_node = None
                        cur.next_node = None
                        cur.elem = None
                        self._size -= 1
                        continue
                    elif val == self._tail.elem:
                        cur.prev_node.next_node = None
                        cur.prev_node = None
                        cur.elem = None
                        self._size -= 1
                        continue
                    else:
                        temp = cur.next_node
                        cur.prev_node.next_node = temp
                        temp.prev_node = cur.prev_node
                        cur.prev_node = None
                        cur.next_node = None
                        cur.elem = None
                        self._size -= 1
                        continue
            return True

        except:
            raise ValueError

    def remove_duplicates(self) -> None:
        """Remove all duplicate occurrences of values from the list."""
        if self._size == 0:
            return None
        cur = self._head
        while cur:
            temp = cur.next_node
            while temp:
                if cur.elem == temp.elem:
                    temp.prev_node.next_node = temp.next_node

                    if temp.next_node != None:
                        temp.next_node.prev_node = temp.prev_node
                    self._size -= 1
                temp = temp.next_node

            cur = cur.next_node



    def filter_n_max(self, n: int) -> None:
        """Filter the list to only contain the 'n' highest values.

        Args:
            n (int): 0 < n <= length of list

        Raises:
            ValueError: If the passed value n is not an int or out of range.
        """
        if not isinstance(n, int) or n < 1 or self._size < 1 or n > self._size:
            raise ValueError
        cur = self._head
        i = 0
        while cur:
            if i + 1 <= self._size - n:
                self._head = cur.next_node
                cur = self._head
                self._size -= 1
            else:
                i += 1
                cur = cur.next_node




    def filter_odd(self) -> None:
        """Filter the list to only contain odd values."""
        # TODO


