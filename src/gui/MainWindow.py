from tkinter import Tk, StringVar
from tkinter.ttk import Frame, Style, OptionMenu, PanedWindow, Label

from src.algos.TrajectorySimilarityCalculator import Calculator


def display():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()


class MainWindow(PanedWindow):

    def __init__(self, root: Tk):
        super().__init__()
        self._init_ui(root)

    def _init_ui(self, root: Tk):
        self.master.title("Trajectory Similarity Calculator")
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        configuration = Frame(root)
        image = Frame(root)

        # Select method
        calculators = StringVar(value=Calculator.DTW)

        label = Label(configuration, text="Selected method")
        menu = OptionMenu(configuration, calculators, *[c.value for c in Calculator])

        label.grid(row=0, column=0, sticky='wn')
        menu.grid(row=1, column=0, sticky='wn')

        configuration.pack(side="left", fill="both", expand=True)
        image.pack(side="right", fill="both", expand=True)

        self.add(configuration)
        self.add(image)

        self.pack(expand=True)
