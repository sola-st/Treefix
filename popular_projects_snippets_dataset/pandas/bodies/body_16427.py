# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
data = np.arange(6)
data_ser = Series(data, dtype="int64")

bins = [-np.inf, 2, 4, np.inf]
result = cut(data, bins)
result_ser = cut(data_ser, bins)

ex_uniques = IntervalIndex.from_breaks(bins)
tm.assert_index_equal(result.categories, ex_uniques)

assert result[5] == Interval(4, np.inf)
assert result[0] == Interval(-np.inf, 2)
assert result_ser[5] == Interval(4, np.inf)
assert result_ser[0] == Interval(-np.inf, 2)
