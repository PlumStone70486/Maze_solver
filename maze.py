import time
import random
from window import *
from cell import *

class Maze:
    def __init__(self, x1, y1, num_cols, num_rows, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_cols = num_cols
        self._num_rows = num_rows
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        
            
        

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                col.append(cell)
            self._cells.append(col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(len(self._cells) - 1, len(self._cells[0]) - 1)

    def _is_in_bounds(self, i, j):
        return 0 <= i < len(self._cells) and 0 <= j < len(self._cells[0])

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            if self._is_in_bounds(i + 1, j):
                if self._cells[i+1][j].visited is False:
                    to_visit.append((i + 1, j))

            if self._is_in_bounds(i, j + 1):
                if self._cells[i][j+1].visited is False:
                    to_visit.append((i, j + 1))

            if self._is_in_bounds(i - 1, j):
                if self._cells[i-1][j].visited is False:
                    to_visit.append((i - 1, j))

            if self._is_in_bounds(i, j - 1):
                if self._cells[i][j-1].visited is False:
                    to_visit.append((i, j - 1))

            if len(to_visit) == 0:
                return
            else:
                chosen_i , chosen_j = random.choice(to_visit)
                chosen_cell = self._cells[chosen_i][chosen_j]

                if chosen_i == i + 1 and chosen_j == j:
                    current_cell.has_bottom_wall = False
                    chosen_cell.has_top_wall = False

                if chosen_i == i and chosen_j == j + 1:
                    current_cell.has_right_wall = False
                    chosen_cell.has_left_wall = False

                if chosen_i == i - 1 and chosen_j == j:
                    current_cell.has_top_wall = False
                    chosen_cell.has_bottom_wall = False

                if chosen_i == i and chosen_j == j - 1:
                    current_cell.has_left_wall = False
                    chosen_cell.has_right_wall = False
                    
                self._draw_cell(i, j)
                self._draw_cell(chosen_i, chosen_j)
                self._break_walls_r(chosen_i, chosen_j)


