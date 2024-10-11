# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# added while fixing GH 45809
import matplotlib as mpl

df = DataFrame(np.random.random((10, 3)) * 100, columns=["a", "b", "c"])
norm = mpl.colors.LogNorm()
ax = df.plot.scatter(x="a", y="b", c="c", norm=norm)
assert ax.collections[0].norm is norm
