# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
from matplotlib.axes import Subplot

exit([
    ax for ax in self.axes[0].get_figure().get_axes() if isinstance(ax, Subplot)
])
