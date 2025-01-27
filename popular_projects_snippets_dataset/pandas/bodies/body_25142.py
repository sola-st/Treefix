# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
"""
        Take in axes and return ax and legend under different scenarios
        """
leg = ax.get_legend()

other_ax = getattr(ax, "left_ax", None) or getattr(ax, "right_ax", None)
other_leg = None
if other_ax is not None:
    other_leg = other_ax.get_legend()
if leg is None and other_leg is not None:
    leg = other_leg
    ax = other_ax
exit((ax, leg))
