# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
from matplotlib import cm

from pandas.plotting import andrews_curves

df = iris
# Ensure no UserWarning when making plot
with tm.assert_produces_warning(None):
    _check_plot_works(andrews_curves, frame=df, class_column="Name")

rgba = ("#556270", "#4ECDC4", "#C7F464")
ax = _check_plot_works(
    andrews_curves, frame=df, class_column="Name", color=rgba
)
self._check_colors(
    ax.get_lines()[:10], linecolors=rgba, mapping=df["Name"][:10]
)

cnames = ["dodgerblue", "aquamarine", "seagreen"]
ax = _check_plot_works(
    andrews_curves, frame=df, class_column="Name", color=cnames
)
self._check_colors(
    ax.get_lines()[:10], linecolors=cnames, mapping=df["Name"][:10]
)

ax = _check_plot_works(
    andrews_curves, frame=df, class_column="Name", colormap=cm.jet
)
cmaps = [cm.jet(n) for n in np.linspace(0, 1, df["Name"].nunique())]
self._check_colors(
    ax.get_lines()[:10], linecolors=cmaps, mapping=df["Name"][:10]
)

length = 10
df = DataFrame(
    {
        "A": np.random.rand(length),
        "B": np.random.rand(length),
        "C": np.random.rand(length),
        "Name": ["A"] * length,
    }
)

_check_plot_works(andrews_curves, frame=df, class_column="Name")

rgba = ("#556270", "#4ECDC4", "#C7F464")
ax = _check_plot_works(
    andrews_curves, frame=df, class_column="Name", color=rgba
)
self._check_colors(
    ax.get_lines()[:10], linecolors=rgba, mapping=df["Name"][:10]
)

cnames = ["dodgerblue", "aquamarine", "seagreen"]
ax = _check_plot_works(
    andrews_curves, frame=df, class_column="Name", color=cnames
)
self._check_colors(
    ax.get_lines()[:10], linecolors=cnames, mapping=df["Name"][:10]
)

ax = _check_plot_works(
    andrews_curves, frame=df, class_column="Name", colormap=cm.jet
)
cmaps = [cm.jet(n) for n in np.linspace(0, 1, df["Name"].nunique())]
self._check_colors(
    ax.get_lines()[:10], linecolors=cmaps, mapping=df["Name"][:10]
)

colors = ["b", "g", "r"]
df = DataFrame({"A": [1, 2, 3], "B": [1, 2, 3], "C": [1, 2, 3], "Name": colors})
ax = andrews_curves(df, "Name", color=colors)
handles, labels = ax.get_legend_handles_labels()
self._check_colors(handles, linecolors=colors)
