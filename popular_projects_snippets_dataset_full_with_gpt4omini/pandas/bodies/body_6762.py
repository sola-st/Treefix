# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
i = IntervalIndex.from_arrays((0, 1, np.nan), (1, 2, np.nan), closed=closed)
assert i[0] == Interval(0.0, 1.0, closed=closed)
assert i[1] == Interval(1.0, 2.0, closed=closed)
assert isna(i[2])

result = i[0:1]
expected = IntervalIndex.from_arrays((0.0,), (1.0,), closed=closed)
tm.assert_index_equal(result, expected)

result = i[0:2]
expected = IntervalIndex.from_arrays((0.0, 1), (1.0, 2.0), closed=closed)
tm.assert_index_equal(result, expected)

result = i[1:3]
expected = IntervalIndex.from_arrays(
    (1.0, np.nan), (2.0, np.nan), closed=closed
)
tm.assert_index_equal(result, expected)
