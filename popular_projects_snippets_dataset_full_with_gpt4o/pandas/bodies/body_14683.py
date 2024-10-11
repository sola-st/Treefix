# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
idx = date_range(start="2014-07-01", freq="M", periods=10)
df = DataFrame(np.random.rand(10, 3), index=idx)

for kind in ["line", "area"]:
    axes = df.plot(kind=kind, subplots=True, sharex=True)
    self._check_axes_shape(axes, axes_num=3, layout=(3, 1))

    for ax in axes[:-2]:
        # GH 7801
        self._check_visible(ax.xaxis)  # xaxis must be visible for grid
        self._check_visible(ax.get_xticklabels(), visible=False)
        self._check_visible(ax.get_xticklabels(minor=True), visible=False)
        self._check_visible(ax.xaxis.get_label(), visible=False)
        self._check_visible(ax.get_yticklabels())

    self._check_visible(axes[-1].xaxis)
    self._check_visible(axes[-1].get_xticklabels())
    self._check_visible(axes[-1].get_xticklabels(minor=True))
    self._check_visible(axes[-1].xaxis.get_label())
    self._check_visible(axes[-1].get_yticklabels())
    self._check_ticks_props(axes, xrot=0)

    axes = df.plot(kind=kind, subplots=True, sharex=False, rot=45, fontsize=7)
    for ax in axes:
        self._check_visible(ax.xaxis)
        self._check_visible(ax.get_xticklabels())
        self._check_visible(ax.get_xticklabels(minor=True))
        self._check_visible(ax.xaxis.get_label())
        self._check_visible(ax.get_yticklabels())
        self._check_ticks_props(ax, xlabelsize=7, xrot=45, ylabelsize=7)
