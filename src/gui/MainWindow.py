from tkinter import Tk, StringVar, Variable
from tkinter import Frame, OptionMenu, PanedWindow, Label

from src.algos.TrajectorySimilarityCalculator import Calculator
from src.algos.CalculatorContext import CalculatorContext
from src.core.Trajectory import Trajectory

from src import BASE_IMAGE_PATH, TRAJECTORY_TIMED

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.image import imread


def display():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()


class MainWindow(PanedWindow):

    def __init__(self, root: Tk):
        super().__init__()
        self._init_ui(root)

        self._context = CalculatorContext(Calculator.DTW.value)

        self._figure = None
        self._plot = None

    def plot_trajectory(self, trajectory: Trajectory):
        self._plot.plot([p.x for p in trajectory.points], [p.y for p in trajectory.points])

    def _init_ui(self, root: Tk):
        self.master.title("Trajectory Similarity Calculator")
        self.master.geometry('900x600')

        mainframe = Frame(root)

        configuration = Frame(mainframe, bd=2)
        image = Frame(mainframe, bd=2)

        # Select method
        current_method = StringVar(value=Calculator.DTW.name)

        def method_selection(event):
            self._context.calculator = Calculator.from_name(name=current_method.get())

        menu = OptionMenu(configuration, current_method, *[option.name for option in Calculator],
                          command=method_selection)

        label = Label(configuration, text="Selected method")

        # Image
        self._figure = Figure()
        self._plot = self._figure.add_subplot(111)

        img = imread(BASE_IMAGE_PATH)
        self._plot.imshow(img)

        for t in TRAJECTORY_TIMED:
            self.plot_trajectory(t)

        # Layouting
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        mainframe.grid(sticky='nsew')

        configuration.grid(row=0, column=0, sticky='nsew')
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)
        mainframe.grid_columnconfigure(1, weight=10)

        configuration.grid_columnconfigure(0, weight=1)
        configuration.grid_columnconfigure(1, weight=1)

        label.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        menu.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        image.grid(row=0, column=1, sticky='nsew')

        canvas = FigureCanvasTkAgg(self._figure, master=image)
        canvas.get_tk_widget().pack(side="top", fill='both', expand=True)
