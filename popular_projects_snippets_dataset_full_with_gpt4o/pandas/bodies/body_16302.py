# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
s = Series([1, 2, 3.5], dtype=float_numpy_dtype)
expected = Series([1, 2, 3.5]).astype(float_numpy_dtype)
tm.assert_series_equal(s, expected)
