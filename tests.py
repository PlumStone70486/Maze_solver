import unittest
from window import *
from maze import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_create_cells1(self):
        num_rows = 12
        num_cols = 16
        margin = 10
        screen_x = 800
        screen_y = 600
        cell_size_x = (screen_x - 2 * margin) / num_cols
        cell_size_y = (screen_y - 2 * margin) / num_rows
        win = Window(screen_x, screen_y)
        m1 = Maze(margin, margin, num_cols, num_rows, cell_size_x, cell_size_y)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_create_cells2(self):
        num_rows = 5
        num_cols = 6
        margin = 10
        screen_x = 800
        screen_y = 600
        cell_size_x = (screen_x - 2 * margin) / num_cols
        cell_size_y = (screen_y - 2 * margin) / num_rows
        win = Window(screen_x, screen_y)
        m1 = Maze(margin, margin, num_cols, num_rows, cell_size_x, cell_size_y)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_create_cells3(self):
        num_rows = 15
        num_cols = 20
        margin = 10
        screen_x = 1000
        screen_y = 700
        cell_size_x = (screen_x - 2 * margin) / num_cols
        cell_size_y = (screen_y - 2 * margin) / num_rows
        win = Window(screen_x, screen_y)
        m1 = Maze(margin, margin, num_cols, num_rows, cell_size_x, cell_size_y)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_maze_cells_reset(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        m1._cells[0][0].visited = True
        m1._cells[num_cols - 1][num_rows - 1].visited = True
        self.assertEqual(
            m1._cells[0][0].visited,
            True,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].visited,
            True,
        )
        m1._reset_cells_visited()
        self.assertEqual(
            m1._cells[0][0].visited,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].visited,
            False,
        )

if __name__ == "__main__":
    unittest.main()