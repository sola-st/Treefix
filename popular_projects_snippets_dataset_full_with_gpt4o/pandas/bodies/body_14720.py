# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_hist_box_by.py
# GH 15079
axes = hist_df.plot.box(column="A", by="C", figsize=figsize)
self._check_axes_shape(axes, axes_num=1, figsize=figsize)
