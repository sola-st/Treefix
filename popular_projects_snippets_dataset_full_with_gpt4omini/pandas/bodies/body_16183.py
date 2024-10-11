# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
s1 = Series([], [], dtype=np.int32)
s2 = Series({"x": 0.0})
tm.assert_series_equal(s1 * s2, Series([np.nan], index=["x"]))
