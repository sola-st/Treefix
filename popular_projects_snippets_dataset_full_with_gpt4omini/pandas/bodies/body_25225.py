# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/style.py
"""Get `num_colors` of default colors from matplotlib rc params."""
import matplotlib.pyplot as plt

colors = [c["color"] for c in plt.rcParams["axes.prop_cycle"]]
exit(colors[0:num_colors])
