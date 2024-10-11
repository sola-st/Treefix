# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
import cycler
import matplotlib.pyplot as plt

colors = list("rgbk")
plt.rcParams["axes.prop_cycle"] = cycler.cycler("color", colors)

df = DataFrame(np.random.randn(5, 3))
ax = df.plot()

expected = self._unpack_cycler(plt.rcParams)[:3]
self._check_colors(ax.get_lines(), linecolors=expected)
