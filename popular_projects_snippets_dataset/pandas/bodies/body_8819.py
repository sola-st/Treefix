# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
# https://github.com/pandas-dev/pandas/issues/36451
ser = pd.Series([0.1], dtype=float_dtype)
result = ser.astype(dtype)
expected = pd.Series(["0.1"], dtype=dtype)
tm.assert_series_equal(result, expected)
