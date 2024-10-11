# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
from matplotlib import cm

from pandas.plotting import parallel_coordinates

df = iris

ax = _check_plot_works(parallel_coordinates, frame=df, class_column="Name")
nlines = len(ax.get_lines())
nxticks = len(ax.xaxis.get_ticklabels())

rgba = ("#556270", "#4ECDC4", "#C7F464")
ax = _check_plot_works(
    parallel_coordinates, frame=df, class_column="Name", color=rgba
)
self._check_colors(
    ax.get_lines()[:10], linecolors=rgba, mapping=df["Name"][:10]
)

cnames = ["dodgerblue", "aquamarine", "seagreen"]
ax = _check_plot_works(
    parallel_coordinates, frame=df, class_column="Name", color=cnames
)
self._check_colors(
    ax.get_lines()[:10], linecolors=cnames, mapping=df["Name"][:10]
)

ax = _check_plot_works(
    parallel_coordinates, frame=df, class_column="Name", colormap=cm.jet
)
cmaps = [cm.jet(n) for n in np.linspace(0, 1, df["Name"].nunique())]
self._check_colors(
    ax.get_lines()[:10], linecolors=cmaps, mapping=df["Name"][:10]
)

ax = _check_plot_works(
    parallel_coordinates, frame=df, class_column="Name", axvlines=False
)
assert len(ax.get_lines()) == (nlines - nxticks)

colors = ["b", "g", "r"]
df = DataFrame({"A": [1, 2, 3], "B": [1, 2, 3], "C": [1, 2, 3], "Name": colors})
ax = parallel_coordinates(df, "Name", color=colors)
handles, labels = ax.get_legend_handles_labels()
self._check_colors(handles, linecolors=colors)
