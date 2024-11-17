from window import *
from cell import *
from maze import *


def main():
    
    num_rows = 3
    num_cols = 4
    margin = 10
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_cols, num_rows, cell_size_x, cell_size_y, win, 10)
    """
    win = Window(800, 600)
    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.draw(100, 100, 200, 200)
    """
    win.wait_for_close()

main()