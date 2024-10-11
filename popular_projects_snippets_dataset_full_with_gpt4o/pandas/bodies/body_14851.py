# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
from matplotlib import cm
from matplotlib.collections import PolyCollection

custom_colors = "rgcby"
df = DataFrame(np.random.rand(5, 5))

ax = df.plot.area(color=custom_colors)
self._check_colors(ax.get_lines(), linecolors=custom_colors)
poly = [o for o in ax.get_children() if isinstance(o, PolyCollection)]
self._check_colors(poly, facecolors=custom_colors)

handles, labels = ax.get_legend_handles_labels()
self._check_colors(handles, facecolors=custom_colors)

for h in handles:
    assert h.get_alpha() is None
tm.close()

ax = df.plot.area(colormap="jet")
jet_colors = [cm.jet(n) for n in np.linspace(0, 1, len(df))]
self._check_colors(ax.get_lines(), linecolors=jet_colors)
poly = [o for o in ax.get_children() if isinstance(o, PolyCollection)]
self._check_colors(poly, facecolors=jet_colors)

handles, labels = ax.get_legend_handles_labels()
self._check_colors(handles, facecolors=jet_colors)
for h in handles:
    assert h.get_alpha() is None
tm.close()

# When stacked=False, alpha is set to 0.5
ax = df.plot.area(colormap=cm.jet, stacked=False)
self._check_colors(ax.get_lines(), linecolors=jet_colors)
poly = [o for o in ax.get_children() if isinstance(o, PolyCollection)]
jet_with_alpha = [(c[0], c[1], c[2], 0.5) for c in jet_colors]
self._check_colors(poly, facecolors=jet_with_alpha)

handles, labels = ax.get_legend_handles_labels()
linecolors = jet_with_alpha
self._check_colors(handles[: len(jet_colors)], linecolors=linecolors)
for h in handles:
    assert h.get_alpha() == 0.5
