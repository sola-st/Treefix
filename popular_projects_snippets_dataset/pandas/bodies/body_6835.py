# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# GH#36310
breaks = np.arange(5)
result = IntervalIndex.from_breaks(breaks)._data
assert result._left.base is None or result._left.base is not result._right.base
