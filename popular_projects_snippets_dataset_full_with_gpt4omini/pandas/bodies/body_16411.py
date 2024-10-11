# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
data = np.array([0.2, 1.4, 2.5, 6.2, 9.7, 2.1, 2.575])
result, bins = cut(data, 4, right=True, retbins=True)

intervals = IntervalIndex.from_breaks(bins.round(3))
expected = Categorical(intervals, ordered=True)
expected = expected.take([0, 0, 0, 2, 3, 0, 0])

tm.assert_categorical_equal(result, expected)
tm.assert_almost_equal(bins, np.array([0.1905, 2.575, 4.95, 7.325, 9.7]))
