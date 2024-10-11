# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_hist_box_by.py
# GH 15079
ax1, ax2, ax3 = hist_df.plot.hist(column="A", by="C", sharey=True)

# share y
assert self.get_y_axis(ax1).joined(ax1, ax2)
assert self.get_y_axis(ax2).joined(ax1, ax2)
assert self.get_y_axis(ax3).joined(ax1, ax3)
assert self.get_y_axis(ax3).joined(ax2, ax3)

# don't share x
assert not self.get_x_axis(ax1).joined(ax1, ax2)
assert not self.get_x_axis(ax2).joined(ax1, ax2)
assert not self.get_x_axis(ax3).joined(ax1, ax3)
assert not self.get_x_axis(ax3).joined(ax2, ax3)
