# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_dtypes.py
s = pd.Series([1, 2, 3], dtype="Int64")
result = s.astype(dtype)
expected = pd.Series([1, 2, 3], dtype=dtype)
tm.assert_series_equal(result, expected)

s = pd.Series([1, 2, 3, None], dtype="Int64")
result = s.astype(dtype)
expected = pd.Series([1, 2, 3, None], dtype=dtype)
tm.assert_series_equal(result, expected)
