# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_hist_box_by.py
# GH 15079
# _check_plot_works adds an ax so catch warning. see GH #13188
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(
        hist_df.plot.hist, column=column, by=by, layout=layout
    )
self._check_axes_shape(axes, axes_num=axes_num, layout=layout)
