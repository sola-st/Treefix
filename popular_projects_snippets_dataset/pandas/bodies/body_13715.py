# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_matplotlib.py
# https://github.com/pandas-dev/pandas/issues/49374
cmap = mpl.colors.ListedColormap([[1, 1, 1], [0, 0, 0]])
df["c"] = df.A + df.B
kwargs = dict(x="A", y="B", c="c", colormap=cmap)
if plot_method == "hexbin":
    kwargs["C"] = kwargs.pop("c")
getattr(df.plot, plot_method)(**kwargs)
