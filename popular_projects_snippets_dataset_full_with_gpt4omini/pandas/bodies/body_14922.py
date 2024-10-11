# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
s = Series([1, 2])
ax = s.plot(style="s", color="C3")
assert ax.lines[0].get_color() == "C3"
