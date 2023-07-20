from typing import List, Tuple

# Using constants might make this more readable.
START = 'S'
EXIT = 'X'
VISITED = '.'
OBSTACLE = '#'
PATH = ' '


class MyMaze:
    """Maze object, used for demonstrating recursive algorithms."""

    def __init__(self, maze_str: str = ''):
        """Initialize Maze.

        Args:
            maze_str (str): Maze represented by a string,
            where rows are separated by newlines (\n).

        Raises:
            ValueError, if maze_str is empty.
        """
        if len(maze_str) == 0:
            raise ValueError
        else:
            # We internally treat this as a List[List[str]], as it makes indexing easier.
            self._maze = list(list(row) for row in maze_str.splitlines())
            self._row_range = len(self._maze)
            self._col_range = len(self._maze[0])
            self._exits: List[Tuple[int, int]] = []
            self._max_recursion_depth = 0

    def find_exits(self, start_row: int, start_col: int, depth: int = 0) -> bool:
        """Find and save all exits into `self._exits` using recursion, save
        the maximum recursion depth into 'self._max_recursion_depth' and mark the maze.

        An exit is an accessible from S empty cell on the outer rims of the maze.

        Args:
            start_row (int): row to start from. 0 represents the topmost cell.
            start_col (int): column to start from; 0 represents the leftmost cell.
            depth (int): Depth of current iteration.

        Raises:
            ValueError: If the starting position is out of range or not walkable path.
        """
        result = False
        if not (0 <= start_row < self._row_range) or not (0 <= start_col < self._col_range):
            return False

        if self._maze[start_row][start_col] == OBSTACLE or self._maze[start_row][start_col] == VISITED:
            return False
        self._max_recursion_depth = max(self._max_recursion_depth, depth)

        if (start_row == 0 or start_row == self._row_range - 1 or start_col == 0 or start_col == self._col_range - 1):
            if self._maze[start_row][start_col] == PATH:
                self._exits.append((start_row, start_col))
                self._maze[start_row][start_col] = EXIT
                return True

        self._maze[start_row][start_col] = VISITED

        directs = [(start_row, start_col + 1), (start_row+1, start_col + 1), (start_row+1, start_col), (start_row+1, start_col - 1), (start_row, start_col - 1), (start_row-1, start_col - 1), (start_row-1, start_col), (start_row-1, start_col + 1)]

        for new_row, new_col in directs:
            if self.find_exits(new_row, new_col, depth + 1):

                result = True

        return result

    def main(self, start_row: int, start_col: int):
        maze_15 = """
        ###############
        # #   #       #
        # # # # #######
        # # # #       #
        # # # ####### #
        # # # #   # # #
        # # # ### # # #
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        #     #     # #
        #############X#
        """
        maze_15 = MyMaze(maze_15)
        maze_15.find_exits(start_row, start_col) #random start

        maze_20 = """
        ####################
        # #  #   #     #    #
        # # ### # ### # # # #
        # #     #   # # # # #
        ### ##### # # # # # #
        #   #   # # # # # # #
        # ### ### # # # # # #
        # # #   # # # # # # #
        # # ### # # # # # # #
        # # #   #   # # # # #
        # # # ### ### # # # #
        # # # #   #   # # # #
        # # # # ### ### # # #
        # # # # #       # # #
        # # # # ######### # #
        # # # # #         # #
        # # # # # ####### # #
        # # # # #         # #
        # # # # ######### # #
        #   #   #         # #
        ###################X#
        """
        maze_20 = MyMaze(maze_20)
        maze_20.find_exits(start_row, start_col) #random start

    @property
    def exits(self) -> List[Tuple[int, int]]:
        """List of tuples of (row, col)-coordinates of currently found exits."""
        return self._exits

    @property
    def max_recursion_depth(self) -> int:
        """Return the maximum recursion depth after executing find_exits()."""
        return self._max_recursion_depth

    def __str__(self) -> str:
        return '\n'.join(''.join(row) for row in self._maze)

    __repr__ = __str__
