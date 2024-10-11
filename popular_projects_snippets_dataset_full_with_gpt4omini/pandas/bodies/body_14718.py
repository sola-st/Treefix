# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_hist_box_by.py
# GH 15079
axes = _check_plot_works(
    hist_df.plot.box, default_axes=True, column=column, by=by, layout=layout
)
self._check_axes_shape(axes, axes_num=axes_num, layout=layout)
