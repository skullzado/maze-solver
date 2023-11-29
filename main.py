from graphics import Line, Point, Window


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(50, 50), Point(100, 100)))
    win.wait_for_close()


main()
