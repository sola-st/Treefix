# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py

# supplied ax itself is a SubplotAxes, but figure contains also
# a plain Axes object (GH11556)
fig, ax = self.plt.subplots()
fig.add_axes([0.2, 0.2, 0.2, 0.2])
Series(np.random.rand(10)).plot(ax=ax)

# supplied ax itself is a plain Axes, but because the cmap keyword
# a new ax is created for the colorbar -> also multiples axes (GH11520)
df = DataFrame({"a": np.random.randn(8), "b": np.random.randn(8)})
fig = self.plt.figure()
ax = fig.add_axes((0, 0, 1, 1))
df.plot(kind="scatter", ax=ax, x="a", y="b", c="a", cmap="hsv")

# other examples
fig, ax = self.plt.subplots()
from mpl_toolkits.axes_grid1 import make_axes_locatable

divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)
Series(np.random.rand(10)).plot(ax=ax)
Series(np.random.rand(10)).plot(ax=cax)

fig, ax = self.plt.subplots()
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

iax = inset_axes(ax, width="30%", height=1.0, loc=3)
Series(np.random.rand(10)).plot(ax=ax)
Series(np.random.rand(10)).plot(ax=iax)
