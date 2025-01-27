# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
df = DataFrame(np.random.rand(10, 3), index=list(string.ascii_letters[:10]))

for kind in ["bar", "barh", "line", "area"]:
    axes = df.plot(kind=kind, subplots=True, sharex=True, legend=True)
    self._check_axes_shape(axes, axes_num=3, layout=(3, 1))
    assert axes.shape == (3,)

    for ax, column in zip(axes, df.columns):
        self._check_legend_labels(ax, labels=[pprint_thing(column)])

    for ax in axes[:-2]:
        self._check_visible(ax.xaxis)  # xaxis must be visible for grid
        self._check_visible(ax.get_xticklabels(), visible=False)
        if kind != "bar":
            # change https://github.com/pandas-dev/pandas/issues/26714
            self._check_visible(ax.get_xticklabels(minor=True), visible=False)
        self._check_visible(ax.xaxis.get_label(), visible=False)
        self._check_visible(ax.get_yticklabels())

    self._check_visible(axes[-1].xaxis)
    self._check_visible(axes[-1].get_xticklabels())
    self._check_visible(axes[-1].get_xticklabels(minor=True))
    self._check_visible(axes[-1].xaxis.get_label())
    self._check_visible(axes[-1].get_yticklabels())

    axes = df.plot(kind=kind, subplots=True, sharex=False)
    for ax in axes:
        self._check_visible(ax.xaxis)
        self._check_visible(ax.get_xticklabels())
        self._check_visible(ax.get_xticklabels(minor=True))
        self._check_visible(ax.xaxis.get_label())
        self._check_visible(ax.get_yticklabels())

    axes = df.plot(kind=kind, subplots=True, legend=False)
    for ax in axes:
        assert ax.get_legend() is None
