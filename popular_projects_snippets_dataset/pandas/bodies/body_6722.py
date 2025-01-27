# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_setops.py
index = monotonic_index(0, 11, closed=closed)

# GH 19101: empty result, same dtype
other = monotonic_index(300, 314, closed=closed)
expected = empty_index(dtype="int64", closed=closed)
result = index.intersection(other, sort=sort)
tm.assert_index_equal(result, expected)

# GH 19101: empty result, different numeric dtypes -> common dtype is float64
other = monotonic_index(300, 314, dtype="float64", closed=closed)
result = index.intersection(other, sort=sort)
expected = other[:0]
tm.assert_index_equal(result, expected)

other = monotonic_index(300, 314, dtype="uint64", closed=closed)
result = index.intersection(other, sort=sort)
tm.assert_index_equal(result, expected)
