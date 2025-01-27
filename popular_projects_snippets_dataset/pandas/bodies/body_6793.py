# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH 20636
index = IntervalIndex.from_arrays(*arrays)

value = index[0].mid + Timedelta("12 hours")
result = index.get_loc(value)
expected = slice(0, 2, None)
assert result == expected

interval = Interval(index[0].left, index[0].right)
result = index.get_loc(interval)
expected = 0
assert result == expected
