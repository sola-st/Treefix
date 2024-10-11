# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/tools.py
"""Call fig.subplots_adjust unless fig has constrained_layout enabled."""
if do_adjust_figure(fig):
    fig.subplots_adjust(*args, **kwargs)
