from typing import Any, Generator, Tuple

from tree_node import TreeNode


class BinarySearchTree:
    """Binary-Search-Tree implemented for didactic reasons."""

    def __init__(self, root: TreeNode = None):
        """Initialize BinarySearchTree.

        Args:
            root (TreeNode, optional): Root of the BST. Defaults to None.
        
        Raises:
            ValueError: root is neither a TreeNode nor None.
        """
        self._root = root
        self._size = 0 if root is None else 1
        self._num_of_comparisons = 0

    def insert(self, key: int, value: Any) -> None:
        """Insert a new node into BST.

        Args:
            key (int): Key which is used for placing the value into the tree.
            value (Any): Value to insert.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is already present in the tree.
        """
        if not isinstance(key, int):
            raise ValueError
        if self._root is None:
            self._root = TreeNode(key,value)
        else:
            ins_node = self._root
            while True:
                if key < ins_node.key:
                    if ins_node.left is None:
                        ins_node.left = TreeNode(key,value)
                        break
                    else:
                        ins_node = ins_node.left
                elif key > ins_node.key:
                    if ins_node.right is None:
                        ins_node.right = TreeNode(key,value)
                        break
                    else:
                        ins_node = ins_node.right
                else:
                    raise KeyError


    def find(self, key: int) -> TreeNode:
        """Return node with given key.

        Args:
            key (int): Key of node.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            TreeNode: Node
        """
        if not isinstance(key, int):
            raise ValueError
        node = self._root
        while node is not None:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
        raise KeyError("Key not present in tree.")


    @property
    def size(self) -> int:
        """Return number of nodes contained in the tree."""







    # If users instead call `len(tree)`, this makes it return the same as `tree.size`
    __len__ = size 

    # This is what gets called when you call e.g. `tree[5]`
    def __getitem__(self, key: int) -> Any:
        """Return value of node with given key.

        Args:
            key (int): Key to look for.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            Any: [description]
        """
        return self.find(key).value

    def remove(self, key: int) -> None:
        """Remove node with given key, maintaining BST-properties.

        Args:
            key (int): Key of node which should be deleted.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.
        """
        pass
        # TODO
       
    # Hint: The following 3 methods can be implemented recursively, and 
    # the keyword `yield from` might be extremely useful here:
    # http://simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-1.html

    # Also, we use a small syntactic sugar here: 
    # https://www.pythoninformer.com/python-language/intermediate-python/short-circuit-evaluation/

    def inorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in inorder."""
        node = node or self._root
        # This is needed in the case that there are no nodes.
        if not node:
            return iter(())
        yield from self._inorder(node)

    def preorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in preorder."""
        node = node or self._root
        if not node:
            return iter(())
        yield from self._preorder(node)

    def postorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in postorder."""
        node = node or self._root
        if not node:
            return iter(())
        yield from self._postorder(node)

    # this allows for e.g. `for node in tree`, or `list(tree)`.
    def __iter__(self) -> Generator[TreeNode, None, None]: 
        yield from self._preorder(self._root)

    @property
    def is_valid(self) -> bool:
        """Return if the tree fulfills BST-criteria."""
        pass
        # TODO

    def return_min_key(self) -> TreeNode:
        """Return the node with the smallest key (None if tree is empty)."""

           
    def find_comparison(self, key: int) -> Tuple[int, int]:
        """Create an inbuilt python list of BST values in preorder and compute the number of comparisons needed for
           finding the key both in the list and in the BST.
           Return the numbers of comparisons for both, the list and the BST
        """
        python_list = list(node.key for node in self._preorder())
        # TODO

    def __repr__(self) -> str:
        return f"BinarySearchTree({list(self._inorder(self._root))})"

    ####################################################
    # Helper Functions
    ####################################################

    def get_root(self):
        return self._root

    def _inorder(self, current_node):
        if current_node is None:
            return []
        left_list = self._inorder(current_node.left)
        right_list = self._inorder(current_node.right)
        return left_list + [current_node] + right_list

    def _preorder(self, current_node):
        if current_node is None:
            return []
        left_list = self._preorder(current_node.left)
        right_list = self._preorder(current_node.right)
        return [current_node] + left_list + right_list

    def _postorder(self, current_node):
        if current_node is None:
            return []
        left_list = self._postorder(current_node.left)
        right_list = self._postorder(current_node.right)
        return left_list + right_list + [current_node]

    # You can of course add your own methods and/or functions!
    # (A method is within a class, a function outside of it.)
