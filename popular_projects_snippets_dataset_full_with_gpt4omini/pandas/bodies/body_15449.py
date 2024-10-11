# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# Just a case here to make obvious what this test class is aimed at
idx = IntervalIndex.from_breaks(range(4))
obj = Series(idx)
val = Interval(0.5, 1.5)

obj[0] = val
assert obj.dtype == "Interval[float64, right]"
