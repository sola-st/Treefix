# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
default_colors = self._unpack_cycler(self.plt.rcParams)

df = DataFrame(np.random.randn(5, 5))
ax = df.plot.hist()
self._check_colors(ax.patches[::10], facecolors=default_colors[:5])
tm.close()

custom_colors = "rgcby"
ax = df.plot.hist(color=custom_colors)
self._check_colors(ax.patches[::10], facecolors=custom_colors)
tm.close()

from matplotlib import cm

# Test str -> colormap functionality
ax = df.plot.hist(colormap="jet")
rgba_colors = [cm.jet(n) for n in np.linspace(0, 1, 5)]
self._check_colors(ax.patches[::10], facecolors=rgba_colors)
tm.close()

# Test colormap functionality
ax = df.plot.hist(colormap=cm.jet)
rgba_colors = [cm.jet(n) for n in np.linspace(0, 1, 5)]
self._check_colors(ax.patches[::10], facecolors=rgba_colors)
tm.close()

ax = df.loc[:, [0]].plot.hist(color="DodgerBlue")
self._check_colors([ax.patches[0]], facecolors=["DodgerBlue"])

ax = df.plot(kind="hist", color="green")
self._check_colors(ax.patches[::10], facecolors=["green"] * 5)
tm.close()
