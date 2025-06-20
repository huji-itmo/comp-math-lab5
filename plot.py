from typing import Callable, List
from matplotlib import pyplot as plt
import numpy as np


def plot_function(
    x: List[float],
    y: List[float],
    func: Callable[[float], float],
    x_0: float,
    file_name: str,
):
    fig, ax = plt.subplots()

    x_plot_min = min(min(x), x_0)
    x_plot_max = max(max(x), x_0)
    x_plot = np.linspace(x_plot_min, x_plot_max, 500)
    y_plot = [func(xi) for xi in x_plot]

    ax.plot(x_plot, y_plot, label="Interpolated Function", color="blue")

    ax.scatter(x, y, color="red", label="Data Points")

    y_0 = func(x_0)

    ax.scatter([x_0], [y_0], color="green", label="x_0 Evaluation", zorder=3)

    ax.axvline(x=x_0, color="green", linestyle="--", linewidth=1)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Interpolation Visualization")
    ax.legend()
    ax.grid(True)

    # Display the plot
    plt.savefig(file_name)
    plt.close()
