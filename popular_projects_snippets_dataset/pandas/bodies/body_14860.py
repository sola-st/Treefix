# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
import matplotlib as mpl

color_tuples = [(0.9, 0, 0, 1), (0, 0.9, 0, 1), (0, 0, 0.9, 1)]
colormap = mpl.colors.ListedColormap(color_tuples)
barplot = DataFrame([[1, 2, 3]]).plot(kind="bar", cmap=colormap)
assert color_tuples == [c.get_facecolor() for c in barplot.patches]
