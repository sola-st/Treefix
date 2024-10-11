# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
# GH 3964
fig, axes = self.plt.subplots(3, 3, sharex=True, sharey=True)
self.plt.subplots_adjust(left=0.05, right=0.95, hspace=0.3, wspace=0.3)
df = DataFrame(
    np.random.randn(10, 9),
    index=date_range(start="2014-07-01", freq="M", periods=10),
)
for i, ax in enumerate(axes.ravel()):
    df[i].plot(ax=ax, fontsize=5)

# Rows other than bottom should not be visible
for ax in axes[0:-1].ravel():
    self._check_visible(ax.get_xticklabels(), visible=False)

# Bottom row should be visible
for ax in axes[-1].ravel():
    self._check_visible(ax.get_xticklabels(), visible=True)

# First column should be visible
for ax in axes[[0, 1, 2], [0]].ravel():
    self._check_visible(ax.get_yticklabels(), visible=True)

# Other columns should not be visible
for ax in axes[[0, 1, 2], [1]].ravel():
    self._check_visible(ax.get_yticklabels(), visible=False)
for ax in axes[[0, 1, 2], [2]].ravel():
    self._check_visible(ax.get_yticklabels(), visible=False)
