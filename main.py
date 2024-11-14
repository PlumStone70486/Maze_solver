from window import *

def main():

    win = Window(800, 600)
    point1 = Point(765, 18)
    point2 = Point(28, 588)
    line = Line(point1, point2)
    win.draw_line(line, "black")
    win.wait_for_close()

main()