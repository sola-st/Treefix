# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(
    {
        "A": np.random.uniform(size=20),
        "B": np.random.uniform(size=20),
        "C": np.arange(20) + np.random.uniform(size=20),
    }
)

ax = df.plot.hexbin(x="A", y="B", gridsize=10)
# TODO: need better way to test. This just does existence.
assert len(ax.collections) == 1

# GH 6951
axes = df.plot.hexbin(x="A", y="B", subplots=True)
# hexbin should have 2 axes in the figure, 1 for plotting and another
# is colorbar
assert len(axes[0].figure.axes) == 2
# return value is single axes
self._check_axes_shape(axes, axes_num=1, layout=(1, 1))
