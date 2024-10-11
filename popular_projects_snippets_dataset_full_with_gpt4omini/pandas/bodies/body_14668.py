# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
tuples = zip(string.ascii_letters[:10], range(10))
df = DataFrame(np.random.rand(10, 3), index=MultiIndex.from_tuples(tuples))
grouped = df.groupby(level=1)
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(grouped.boxplot, return_type="axes")
self._check_axes_shape(list(axes.values), axes_num=10, layout=(4, 3))

axes = _check_plot_works(grouped.boxplot, subplots=False, return_type="axes")
self._check_axes_shape(axes, axes_num=1, layout=(1, 1))
