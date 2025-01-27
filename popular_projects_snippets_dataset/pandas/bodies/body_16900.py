# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_qcut.py
# see gh-19768
intervals = IntervalIndex.from_tuples(
    [(ser[0] - Nano(), ser[2] - Day()), np.nan, (ser[2] - Day(), ser[2])]
)
expected = Series(Categorical(intervals, ordered=True))

result = qcut(ser, 2)
tm.assert_series_equal(result, expected)
