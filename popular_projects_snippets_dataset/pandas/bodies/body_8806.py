# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
# Don't compare arrays (37974)
ser = pd.Series(["1.1", pd.NA, "3.3"], dtype=dtype)
result = ser.astype(any_float_dtype)
expected = pd.Series([1.1, np.nan, 3.3], dtype=any_float_dtype)
tm.assert_series_equal(result, expected)
