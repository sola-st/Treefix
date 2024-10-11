# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# GH37454
xlims = (3, 1)
ax = Series([1, 2], index=index).plot(xlim=(xlims))
assert ax.get_xlim() == (3, 1)
