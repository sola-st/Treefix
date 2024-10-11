# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
df = hist_df
# GH4089
ax1, ax2 = df.hist(column="height", by=df.gender, sharex=True)

# share x
assert self.get_x_axis(ax1).joined(ax1, ax2)
assert self.get_x_axis(ax2).joined(ax1, ax2)

# don't share y
assert not self.get_y_axis(ax1).joined(ax1, ax2)
assert not self.get_y_axis(ax2).joined(ax1, ax2)
