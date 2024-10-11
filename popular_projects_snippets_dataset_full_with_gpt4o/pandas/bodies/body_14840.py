# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
import matplotlib.pyplot as plt

default_colors = self._unpack_cycler(plt.rcParams)

df = DataFrame(np.random.randn(5, 5))
ax = df.plot.bar()
self._check_colors(ax.patches[::5], facecolors=default_colors[:5])
tm.close()

custom_colors = "rgcby"
ax = df.plot.bar(color=custom_colors)
self._check_colors(ax.patches[::5], facecolors=custom_colors)
tm.close()

from matplotlib import cm

# Test str -> colormap functionality
ax = df.plot.bar(colormap="jet")
rgba_colors = [cm.jet(n) for n in np.linspace(0, 1, 5)]
self._check_colors(ax.patches[::5], facecolors=rgba_colors)
tm.close()

# Test colormap functionality
ax = df.plot.bar(colormap=cm.jet)
rgba_colors = [cm.jet(n) for n in np.linspace(0, 1, 5)]
self._check_colors(ax.patches[::5], facecolors=rgba_colors)
tm.close()

ax = df.loc[:, [0]].plot.bar(color="DodgerBlue")
self._check_colors([ax.patches[0]], facecolors=["DodgerBlue"])
tm.close()

ax = df.plot(kind="bar", color="green")
self._check_colors(ax.patches[::5], facecolors=["green"] * 5)
tm.close()
