# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# GH 27758
df = Series(dtype=int)
assert df.empty
ax = df.plot()
assert len(ax.get_lines()) == 1
line = ax.get_lines()[0]
assert len(line.get_xdata()) == 0
assert len(line.get_ydata()) == 0
