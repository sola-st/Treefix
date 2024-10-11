# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
# GH 6970, GH 7069
df = hist_df

# check warning to ignore sharex / sharey
# this check should be done in the first function which
# passes multiple axes to plot, hist or boxplot
# location should be changed if other test is added
# which has earlier alphabetical order
with tm.assert_produces_warning(UserWarning):
    fig, axes = self.plt.subplots(2, 2)
    df.groupby("category").boxplot(column="height", return_type="axes", ax=axes)
    self._check_axes_shape(self.plt.gcf().axes, axes_num=4, layout=(2, 2))

fig, axes = self.plt.subplots(2, 3)
with tm.assert_produces_warning(UserWarning):
    returned = df.boxplot(
        column=["height", "weight", "category"],
        by="gender",
        return_type="axes",
        ax=axes[0],
    )
returned = np.array(list(returned.values))
self._check_axes_shape(returned, axes_num=3, layout=(1, 3))
tm.assert_numpy_array_equal(returned, axes[0])
assert returned[0].figure is fig

# draw on second row
with tm.assert_produces_warning(UserWarning):
    returned = df.groupby("classroom").boxplot(
        column=["height", "weight", "category"], return_type="axes", ax=axes[1]
    )
returned = np.array(list(returned.values))
self._check_axes_shape(returned, axes_num=3, layout=(1, 3))
tm.assert_numpy_array_equal(returned, axes[1])
assert returned[0].figure is fig

msg = "The number of passed axes must be 3, the same as the output plot"
with pytest.raises(ValueError, match=msg):
    fig, axes = self.plt.subplots(2, 3)
    # pass different number of axes from required
    with tm.assert_produces_warning(UserWarning):
        axes = df.groupby("classroom").boxplot(ax=axes)
