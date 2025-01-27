# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
df = hist_df
msg = "Layout of 1x1 must be larger than required size 2"
with pytest.raises(ValueError, match=msg):
    df.hist(column="weight", by=df.gender, layout=(1, 1))

msg = "Layout of 1x3 must be larger than required size 4"
with pytest.raises(ValueError, match=msg):
    df.hist(column="height", by=df.category, layout=(1, 3))

msg = "At least one dimension of layout must be positive"
with pytest.raises(ValueError, match=msg):
    df.hist(column="height", by=df.category, layout=(-1, -1))

with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(
        df.hist, column="height", by=df.gender, layout=(2, 1)
    )
self._check_axes_shape(axes, axes_num=2, layout=(2, 1))

with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(
        df.hist, column="height", by=df.gender, layout=(2, -1)
    )
self._check_axes_shape(axes, axes_num=2, layout=(2, 1))

axes = df.hist(column="height", by=df.category, layout=(4, 1))
self._check_axes_shape(axes, axes_num=4, layout=(4, 1))

axes = df.hist(column="height", by=df.category, layout=(-1, 1))
self._check_axes_shape(axes, axes_num=4, layout=(4, 1))

axes = df.hist(column="height", by=df.category, layout=(4, 2), figsize=(12, 8))
self._check_axes_shape(axes, axes_num=4, layout=(4, 2), figsize=(12, 8))
tm.close()

# GH 6769
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(
        df.hist, column="height", by="classroom", layout=(2, 2)
    )
self._check_axes_shape(axes, axes_num=3, layout=(2, 2))

# without column
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(df.hist, by="classroom")
self._check_axes_shape(axes, axes_num=3, layout=(2, 2))

axes = df.hist(by="gender", layout=(3, 5))
self._check_axes_shape(axes, axes_num=2, layout=(3, 5))

axes = df.hist(column=["height", "weight", "category"])
self._check_axes_shape(axes, axes_num=3, layout=(2, 2))
