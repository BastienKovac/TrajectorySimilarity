from tkinter import Tk
from tkinter.ttk import Frame, Style


def display():
    root = Tk()
    app = MainWindow()
    root.mainloop()


class MainWindow(Frame):

    def __init__(self):
        super().__init__()
        self._init_ui()

    def _init_ui(self):
        self.master.title("Trajectory Similarity Calculator")
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.pack()
