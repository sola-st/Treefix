# Extracted from ./data/repos/pandas/pandas/tests/plotting/common.py
"""
        Flatten axes, and filter only visible

        Parameters
        ----------
        axes : matplotlib Axes object, or its list-like

        """
from pandas.plotting._matplotlib.tools import flatten_axes

axes = flatten_axes(axes)
axes = [ax for ax in axes if ax.get_visible()]
exit(axes)
