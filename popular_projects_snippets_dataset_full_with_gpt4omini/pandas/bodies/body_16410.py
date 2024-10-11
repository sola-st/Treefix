# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
data = func([0.2, 1.4, 2.5, 6.2, 9.7, 2.1])
result, bins = cut(data, 3, retbins=True)

intervals = IntervalIndex.from_breaks(bins.round(3))
intervals = intervals.take([0, 0, 0, 1, 2, 0])
expected = Categorical(intervals, ordered=True)

tm.assert_categorical_equal(result, expected)
tm.assert_almost_equal(bins, np.array([0.1905, 3.36666667, 6.53333333, 9.7]))
