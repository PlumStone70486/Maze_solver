from window import *
from cell import *
from maze import *
import sys
import random


def main():
    
    num_rows = 10
    num_cols = 12
    margin = 10
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    seed = random.randrange(1, 100)
    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_cols, num_rows, cell_size_x, cell_size_y, win, seed)
    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()

main()