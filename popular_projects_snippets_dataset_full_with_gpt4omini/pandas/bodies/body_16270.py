# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
result = Series([1.0, 2.0, np.nan], dtype=string_dtype)
expected = Series(["1.0", "2.0", np.nan], dtype=object)
tm.assert_series_equal(result, expected)
assert np.isnan(result[2])
