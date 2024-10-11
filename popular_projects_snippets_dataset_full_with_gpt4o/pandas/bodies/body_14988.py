# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
from matplotlib import cm

from pandas.plotting import radviz

df = iris
# Ensure no UserWarning when making plot
with tm.assert_produces_warning(None):
    _check_plot_works(radviz, frame=df, class_column="Name")

rgba = ("#556270", "#4ECDC4", "#C7F464")
ax = _check_plot_works(radviz, frame=df, class_column="Name", color=rgba)
# skip Circle drawn as ticks
patches = [p for p in ax.patches[:20] if p.get_label() != ""]
self._check_colors(patches[:10], facecolors=rgba, mapping=df["Name"][:10])

cnames = ["dodgerblue", "aquamarine", "seagreen"]
_check_plot_works(radviz, frame=df, class_column="Name", color=cnames)
patches = [p for p in ax.patches[:20] if p.get_label() != ""]
self._check_colors(patches, facecolors=cnames, mapping=df["Name"][:10])

_check_plot_works(radviz, frame=df, class_column="Name", colormap=cm.jet)
cmaps = [cm.jet(n) for n in np.linspace(0, 1, df["Name"].nunique())]
patches = [p for p in ax.patches[:20] if p.get_label() != ""]
self._check_colors(patches, facecolors=cmaps, mapping=df["Name"][:10])

colors = [[0.0, 0.0, 1.0, 1.0], [0.0, 0.5, 1.0, 1.0], [1.0, 0.0, 0.0, 1.0]]
df = DataFrame(
    {"A": [1, 2, 3], "B": [2, 1, 3], "C": [3, 2, 1], "Name": ["b", "g", "r"]}
)
ax = radviz(df, "Name", color=colors)
handles, labels = ax.get_legend_handles_labels()
self._check_colors(handles, facecolors=colors)
