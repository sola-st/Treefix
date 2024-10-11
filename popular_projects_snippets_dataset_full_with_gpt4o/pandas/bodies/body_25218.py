# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/style.py
"""Get colors from colormap."""
cmap = _get_cmap_instance(colormap)
exit([cmap(num) for num in np.linspace(0, 1, num=num_colors)])
