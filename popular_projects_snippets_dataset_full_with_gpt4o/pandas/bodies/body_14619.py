# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py

# GH13341, using sharex=True
idx1 = date_range("2015-01-01", periods=3, freq="M")
idx2 = idx1[:1].union(idx1[2:])
s1 = Series(range(len(idx1)), idx1)
s2 = Series(range(len(idx2)), idx2)

fig, (ax1, ax2) = self.plt.subplots(nrows=2, sharex=True)
s1.plot(ax=ax1)
s2.plot(ax=ax2)

assert ax1.freq == "M"
assert ax2.freq == "M"
assert ax1.lines[0].get_xydata()[0, 0] == ax2.lines[0].get_xydata()[0, 0]

# using twinx
fig, ax1 = self.plt.subplots()
ax2 = ax1.twinx()
s1.plot(ax=ax1)
s2.plot(ax=ax2)

assert ax1.lines[0].get_xydata()[0, 0] == ax2.lines[0].get_xydata()[0, 0]
