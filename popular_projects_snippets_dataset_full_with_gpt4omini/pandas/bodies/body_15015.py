# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
df = hist_df

# _check_plot_works adds an `ax` kwarg to the method call
# so we get a warning about an axis being cleared, even
# though we don't explicing pass one, see GH #13188
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(df.height.hist, by=df.gender, layout=(2, 1))
self._check_axes_shape(axes, axes_num=2, layout=(2, 1))

with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(df.height.hist, by=df.gender, layout=(3, -1))
self._check_axes_shape(axes, axes_num=2, layout=(3, 1))

with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(df.height.hist, by=df.category, layout=(4, 1))
self._check_axes_shape(axes, axes_num=4, layout=(4, 1))

with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(df.height.hist, by=df.category, layout=(2, -1))
self._check_axes_shape(axes, axes_num=4, layout=(2, 2))

with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(df.height.hist, by=df.category, layout=(3, -1))
self._check_axes_shape(axes, axes_num=4, layout=(3, 2))

with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(df.height.hist, by=df.category, layout=(-1, 4))
self._check_axes_shape(axes, axes_num=4, layout=(1, 4))

with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(df.height.hist, by=df.classroom, layout=(2, 2))
self._check_axes_shape(axes, axes_num=3, layout=(2, 2))

axes = df.height.hist(by=df.category, layout=(4, 2), figsize=(12, 7))
self._check_axes_shape(axes, axes_num=4, layout=(4, 2), figsize=(12, 7))
