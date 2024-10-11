# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
from matplotlib import cm

default_colors = self._unpack_cycler(self.plt.rcParams)

df = DataFrame(np.random.randn(5, 5))

axes = df.plot(kind="kde", subplots=True)
for ax, c in zip(axes, list(default_colors)):
    self._check_colors(ax.get_lines(), linecolors=[c])
tm.close()

# single color char
axes = df.plot(kind="kde", color="k", subplots=True)
for ax in axes:
    self._check_colors(ax.get_lines(), linecolors=["k"])
tm.close()

# single color str
axes = df.plot(kind="kde", color="red", subplots=True)
for ax in axes:
    self._check_colors(ax.get_lines(), linecolors=["red"])
tm.close()

custom_colors = "rgcby"
axes = df.plot(kind="kde", color=custom_colors, subplots=True)
for ax, c in zip(axes, list(custom_colors)):
    self._check_colors(ax.get_lines(), linecolors=[c])
tm.close()

rgba_colors = [cm.jet(n) for n in np.linspace(0, 1, len(df))]
for cmap in ["jet", cm.jet]:
    axes = df.plot(kind="kde", colormap=cmap, subplots=True)
    for ax, c in zip(axes, rgba_colors):
        self._check_colors(ax.get_lines(), linecolors=[c])
    tm.close()

# make color a list if plotting one column frame
# handles cases like df.plot(color='DodgerBlue')
axes = df.loc[:, [0]].plot(kind="kde", color="DodgerBlue", subplots=True)
self._check_colors(axes[0].lines, linecolors=["DodgerBlue"])

# single character style
axes = df.plot(kind="kde", style="r", subplots=True)
for ax in axes:
    self._check_colors(ax.get_lines(), linecolors=["r"])
tm.close()

# list of styles
styles = list("rgcby")
axes = df.plot(kind="kde", style=styles, subplots=True)
for ax, c in zip(axes, styles):
    self._check_colors(ax.get_lines(), linecolors=[c])
tm.close()
