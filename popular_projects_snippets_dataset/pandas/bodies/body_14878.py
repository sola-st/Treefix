# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
fig, ax = self.plt.subplots()
ax = ts.plot(ax=ax)
xmin, xmax = ax.get_xlim()
lines = ax.get_lines()
assert xmin <= lines[0].get_data(orig=False)[0][0]
assert xmax >= lines[0].get_data(orig=False)[0][-1]
tm.close()

ax = ts.plot(secondary_y=True, ax=ax)
xmin, xmax = ax.get_xlim()
lines = ax.get_lines()
assert xmin <= lines[0].get_data(orig=False)[0][0]
assert xmax >= lines[0].get_data(orig=False)[0][-1]
