# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# https://github.com/pandas-dev/pandas/issues/21083
ser = Series(["x", None], dtype=string_dtype)
result = ser.isna()
expected = Series([False, True])
tm.assert_series_equal(result, expected)
assert ser.iloc[1] is None

ser = Series(["x", np.nan], dtype=string_dtype)
assert np.isnan(ser.iloc[1])
