import matplotlib.pyplot as plt
from collections import Counter

class Plotter:
    background = "#36393F"
    accent = "#FFFFFF"
    main_color = "#7289DA"
    main_font = {'fontname':'Whitney'}

    def __init__(self) -> None:
        self.fig = None
        self.ax = None

    def default_graph(graph_function):
        fig, ax = plt.subplots()
        # General plot size
        fig.set_figheight(2.5)
        fig.subplots_adjust(bottom=0.12, left=0.08, right=0.97)

        # Colors
        ax.set_facecolor(Plotter.background)
        fig.set_facecolor(Plotter.background)
        
        ax.spines[:].set_color(Plotter.accent)
        ax.tick_params(axis='x', colors=Plotter.accent, which="both")
        ax.tick_params(axis='y', colors=Plotter.accent, which="both")
        
        ax.yaxis.label.set_color(Plotter.accent)
        ax.xaxis.label.set_color(Plotter.accent)
        ax.title.set_color(Plotter.accent)

        def wrapper(self, *args, **kwargs):
            # Kwargs handling
            # Set title and labels
            title = kwargs.pop('title', "")
            x_label = kwargs.pop('x_label', "")
            y_label = kwargs.pop('y_label', "")

            ax.set_title(title, fontsize=18)
            ax.set_xlabel(x_label)
            ax.set_ylabel(y_label)
            
            # Turn grid on using which (major, minor, both)
            grid = kwargs.pop('grid', None)
            if grid:
                ax.grid(True, grid, color=Plotter.accent)
            
            self.fig = fig
            self.ax = ax
            result = graph_function(self, *args, **kwargs)
            plt.show()

            return result
        return wrapper

    @default_graph
    def bar_graph(self, data, **kwargs):
        counter = Counter(data)
        self.ax.bar(counter.keys(), counter.values(), **kwargs)

