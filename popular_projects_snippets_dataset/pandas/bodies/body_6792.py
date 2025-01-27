# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH 20636
# nonoverlapping = IntervalIndex method and no i8 conversion
index = IntervalIndex.from_breaks(breaks)

value = index[0].mid
result = index.get_loc(value)
expected = 0
assert result == expected

interval = Interval(index[0].left, index[0].right)
result = index.get_loc(interval)
expected = 0
assert result == expected
