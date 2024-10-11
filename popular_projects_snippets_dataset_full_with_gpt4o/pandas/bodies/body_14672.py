# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
df = hist_df

msg = "Layout of 1x1 must be larger than required size 2"
with pytest.raises(ValueError, match=msg):
    df.boxplot(column=["weight", "height"], by=df.gender, layout=(1, 1))

msg = "The 'layout' keyword is not supported when 'by' is None"
with pytest.raises(ValueError, match=msg):
    df.boxplot(
        column=["height", "weight", "category"],
        layout=(2, 1),
        return_type="dict",
    )

msg = "At least one dimension of layout must be positive"
with pytest.raises(ValueError, match=msg):
    df.boxplot(column=["weight", "height"], by=df.gender, layout=(-1, -1))

# _check_plot_works adds an ax so catch warning. see GH #13188
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    box = _check_plot_works(
        df.groupby("gender").boxplot, column="height", return_type="dict"
    )
self._check_axes_shape(self.plt.gcf().axes, axes_num=2, layout=(1, 2))

with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    box = _check_plot_works(
        df.groupby("category").boxplot, column="height", return_type="dict"
    )
self._check_axes_shape(self.plt.gcf().axes, axes_num=4, layout=(2, 2))

# GH 6769
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    box = _check_plot_works(
        df.groupby("classroom").boxplot, column="height", return_type="dict"
    )
self._check_axes_shape(self.plt.gcf().axes, axes_num=3, layout=(2, 2))

# GH 5897
axes = df.boxplot(
    column=["height", "weight", "category"], by="gender", return_type="axes"
)
self._check_axes_shape(self.plt.gcf().axes, axes_num=3, layout=(2, 2))
for ax in [axes["height"]]:
    self._check_visible(ax.get_xticklabels(), visible=False)
    self._check_visible([ax.xaxis.get_label()], visible=False)
for ax in [axes["weight"], axes["category"]]:
    self._check_visible(ax.get_xticklabels())
    self._check_visible([ax.xaxis.get_label()])

box = df.groupby("classroom").boxplot(
    column=["height", "weight", "category"], return_type="dict"
)
self._check_axes_shape(self.plt.gcf().axes, axes_num=3, layout=(2, 2))

with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    box = _check_plot_works(
        df.groupby("category").boxplot,
        column="height",
        layout=(3, 2),
        return_type="dict",
    )
self._check_axes_shape(self.plt.gcf().axes, axes_num=4, layout=(3, 2))
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    box = _check_plot_works(
        df.groupby("category").boxplot,
        column="height",
        layout=(3, -1),
        return_type="dict",
    )
self._check_axes_shape(self.plt.gcf().axes, axes_num=4, layout=(3, 2))

box = df.boxplot(
    column=["height", "weight", "category"], by="gender", layout=(4, 1)
)
self._check_axes_shape(self.plt.gcf().axes, axes_num=3, layout=(4, 1))

box = df.boxplot(
    column=["height", "weight", "category"], by="gender", layout=(-1, 1)
)
self._check_axes_shape(self.plt.gcf().axes, axes_num=3, layout=(3, 1))

box = df.groupby("classroom").boxplot(
    column=["height", "weight", "category"], layout=(1, 4), return_type="dict"
)
self._check_axes_shape(self.plt.gcf().axes, axes_num=3, layout=(1, 4))

box = df.groupby("classroom").boxplot(  # noqa
    column=["height", "weight", "category"], layout=(1, -1), return_type="dict"
)
self._check_axes_shape(self.plt.gcf().axes, axes_num=3, layout=(1, 3))
