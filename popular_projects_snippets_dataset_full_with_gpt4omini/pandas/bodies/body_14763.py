# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# added while fixing GH 45809
import matplotlib as mpl

df = DataFrame(np.random.random((10, 3)) * 100, columns=["a", "b", "c"])
ax = df.plot.scatter(x="a", y="b", c="c")
plot_norm = ax.collections[0].norm
color_min_max = (df.c.min(), df.c.max())
default_norm = mpl.colors.Normalize(*color_min_max)
for value in df.c:
    assert plot_norm(value) == default_norm(value)
