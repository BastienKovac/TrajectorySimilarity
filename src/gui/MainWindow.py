from tkinter import Tk, StringVar, IntVar
from tkinter import Frame, OptionMenu, PanedWindow, Label, Button, Checkbutton

from src.algos.CalculatorContext import CalculatorContext, Calculator
from src.core.Trajectory import Trajectory

from src import BASE_IMAGE_PATH, QUERIES_FULL, QUERIES_SPARSE, TRAJECTORY_TIMED, TRAJECTORY_UNTIMED

import matplotlib.patches as mpatches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.image import imread

import re
import time

import matplotlib
matplotlib.use("TkAgg")


def display():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()


class MainWindow(PanedWindow):

    def __init__(self, root: Tk):
        super().__init__()

        self._figure = None
        self._plot = None
        self._canvas = None

        self._init_ui(root)

        self._context = CalculatorContext(Calculator.DTW.value)
        self._query = QUERIES_FULL[0]
        self._result = None

        self._debug = False

        self.reset_image()

    def plot_trajectory(self, trajectory: Trajectory, color: str = 'red'):
        self._plot.plot([p.x for p in trajectory.points], [p.y for p in trajectory.points], c=color)

    def reset_image(self):
        self._figure.clf()

        self._plot = self._figure.add_subplot(111)

        img = imread(BASE_IMAGE_PATH)
        self._plot.imshow(img)

        self.plot_trajectory(self._query, color='red')

        query_patch = mpatches.Patch(color='red', label="Queried Trajectory")
        legends = [query_patch]

        if self._result:
            self.plot_trajectory(self._result, color='blue')
            legends.append(mpatches.Patch(color='blue', label="Closest computed Trajectory"))

        if self._debug:
            for trajectory in TRAJECTORY_TIMED:
                if trajectory != self._result:
                    self.plot_trajectory(trajectory, color='yellow')

            legends.append(mpatches.Patch(color='yellow', label="Other trajectories"))

        self._plot.legend(handles=legends)
        self._canvas.draw()

    def _init_ui(self, root: Tk):
        self.master.title("Trajectory Similarity Calculator")
        self.master.geometry('900x600')

        mainframe = Frame(root)

        configuration = Frame(mainframe, bd=2)
        image = Frame(mainframe, bd=2)

        # Select method
        current_method = StringVar(value=Calculator.DTW.name)

        def method_selection(event):
            self._context.calculator = Calculator.from_name(name=current_method.get()).value
            self._result = None
            self.reset_image()

        menu = OptionMenu(configuration, current_method, *[option.name for option in Calculator],
                          command=method_selection)

        label = Label(configuration, text="Selected method", anchor='w')

        # Select request
        query_label = Label(configuration, text="Select Query", anchor='w')

        current_query = StringVar(value="Query Full ({})".format(1))

        def query_selection(event):
            selected = current_query.get()
            index = int(re.search(r'\d+', selected).group()) - 1
            if "Full" in selected:
                self._query = QUERIES_FULL[index]
            elif "Sparse" in selected:
                self._query = QUERIES_SPARSE[index]

            self._result = None
            self.reset_image()

        options = []
        for i in range(len(QUERIES_FULL)):
            options.append("Query Full ({})".format(i + 1))
        for i in range(len(QUERIES_SPARSE)):
            options.append("Query Sparse ({})".format(i + 1))

        query_menu = OptionMenu(configuration, current_query, *options, command=query_selection)

        time_label = Label(configuration, text="Last Execution time: ", anchor='w')

        # Find closest trajectory button
        def compute_button():
            start = time.time()

            all_trajectories = [t for t in TRAJECTORY_TIMED]
            if not self._context.calculator.needs_timed_trajectory():
                all_trajectories.extend([t for t in TRAJECTORY_UNTIMED])

            result = self._context.compute_similarity(self._query, all_trajectories)

            sorted_result = sorted(result.items(), key=lambda x: x[1])
            self._result = sorted_result[0][0]

            elapsed_time = time.time() - start

            time_label['text'] = "Last Execution time: {} ms".format(elapsed_time * 1000.0)
            self.reset_image()

        button = Button(configuration, text='Find closest trajectory', command=compute_button)

        # Display other trajectories
        debug = IntVar()

        def checkbox_callback():
            self._debug = debug.get() == 1
            self.reset_image()

        checkbox = Checkbutton(configuration, text='Display all trajectories', variable=debug, onvalue=1, offvalue=0,
                               command=checkbox_callback)

        # Image
        self._figure = Figure()

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

        label.grid(row=0, column=0, sticky='nsw', padx=10, pady=10)
        menu.grid(row=0, column=1, sticky='nsw', padx=10, pady=10)

        query_label.grid(row=1, column=0, sticky='nsw', padx=10, pady=10)
        query_menu.grid(row=1, column=1, sticky='nsw', padx=10, pady=10)

        button.grid(row=2, column=1, sticky='nsw', padx=10, pady=10)

        checkbox.grid(row=3, column=0, sticky='nsw', padx=10, pady=10)

        time_label.grid(row=4, column=0, sticky='nsw', padx=10, pady=10)

        image.grid(row=0, column=1, sticky='nsew')

        self._canvas = FigureCanvasTkAgg(self._figure, master=image)
        self._canvas.get_tk_widget().pack(side="top", fill='both', expand=True)
