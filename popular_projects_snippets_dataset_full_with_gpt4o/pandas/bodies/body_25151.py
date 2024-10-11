# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
import matplotlib.pyplot as plt

if ax is None and len(plt.get_fignums()) > 0:
    with plt.rc_context():
        ax = plt.gca()
    ax = cls._get_ax_layer(ax)
