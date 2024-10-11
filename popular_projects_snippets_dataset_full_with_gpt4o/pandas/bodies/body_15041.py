# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
# GH 6970, GH 7069
df = hist_df

fig, axes = self.plt.subplots(2, 3)
returned = df.hist(column=["height", "weight", "category"], ax=axes[0])
self._check_axes_shape(returned, axes_num=3, layout=(1, 3))
tm.assert_numpy_array_equal(returned, axes[0])
assert returned[0].figure is fig
returned = df.hist(by="classroom", ax=axes[1])
self._check_axes_shape(returned, axes_num=3, layout=(1, 3))
tm.assert_numpy_array_equal(returned, axes[1])
assert returned[0].figure is fig

fig, axes = self.plt.subplots(2, 3)
# pass different number of axes from required
msg = "The number of passed axes must be 1, the same as the output plot"
with pytest.raises(ValueError, match=msg):
    axes = df.hist(column="height", ax=axes)
