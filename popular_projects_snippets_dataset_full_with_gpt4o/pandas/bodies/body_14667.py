# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
grouped = hist_df.groupby(by="gender")
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(grouped.boxplot, return_type="axes")
self._check_axes_shape(list(axes.values), axes_num=2, layout=(1, 2))
axes = _check_plot_works(grouped.boxplot, subplots=False, return_type="axes")
self._check_axes_shape(axes, axes_num=1, layout=(1, 1))
