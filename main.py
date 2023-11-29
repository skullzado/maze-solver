from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.title = self.root_widget.title
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
