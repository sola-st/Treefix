# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# check that we return NotImplemented when operating with Series
# or DataFrame
index = RangeIndex(5)
other = Series(np.random.randn(5))

expected = op(Series(index), other)
result = op(index, other)
tm.assert_series_equal(result, expected)

other = pd.DataFrame(np.random.randn(2, 5))
expected = op(pd.DataFrame([index, index]), other)
result = op(index, other)
tm.assert_frame_equal(result, expected)
