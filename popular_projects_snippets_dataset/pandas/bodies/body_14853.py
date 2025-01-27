# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
from matplotlib import cm

custom_colors = "rgcby"
df = DataFrame(np.random.rand(5, 5))

ax = df.plot.kde(color=custom_colors)
self._check_colors(ax.get_lines(), linecolors=custom_colors)
tm.close()

ax = df.plot.kde(colormap="jet")
rgba_colors = [cm.jet(n) for n in np.linspace(0, 1, len(df))]
self._check_colors(ax.get_lines(), linecolors=rgba_colors)
tm.close()

ax = df.plot.kde(colormap=cm.jet)
rgba_colors = [cm.jet(n) for n in np.linspace(0, 1, len(df))]
self._check_colors(ax.get_lines(), linecolors=rgba_colors)
