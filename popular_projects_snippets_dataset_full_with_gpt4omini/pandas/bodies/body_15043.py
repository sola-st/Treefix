# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
df = hist_df
ax1, ax2 = df.hist(column="height", by=df.gender, sharey=True)

# share y
assert self.get_y_axis(ax1).joined(ax1, ax2)
assert self.get_y_axis(ax2).joined(ax1, ax2)

# don't share x
assert not self.get_x_axis(ax1).joined(ax1, ax2)
assert not self.get_x_axis(ax2).joined(ax1, ax2)
