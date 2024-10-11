# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#9144, inf signing
ser = Series([-1, 0, 1], name="first")
expected = Series([-np.inf, np.nan, np.inf], name="first")

result = ser / 0
tm.assert_series_equal(result, expected)
