# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
# GH 6279 - Series histogram can have a legend
index = 15 * ["1"] + 15 * ["2"]
s = Series(np.random.randn(30), index=index, name="a")
s.index.name = "b"

# Use default_axes=True when plotting method generate subplots itself
axes = _check_plot_works(s.hist, default_axes=True, legend=True, by=by)
self._check_axes_shape(axes, axes_num=expected_axes_num, layout=expected_layout)
self._check_legend_labels(axes, "a")
