# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
s = Series([0, 1, 2], index=[1, 2, 3], name="x")
np.add.at(s, [0, 2], 10)
expected = Series([10, 1, 12], index=[1, 2, 3], name="x")
tm.assert_series_equal(s, expected)
