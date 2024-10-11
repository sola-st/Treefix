# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_function.py
# https://github.com/pandas-dev/pandas/issues/33317
ser = pd.Series([], dtype="Int64")
result = ser.value_counts()
idx = pd.Index([], dtype=ser.dtype)
assert idx.dtype == ser.dtype
expected = pd.Series([], index=idx, dtype="Int64")
tm.assert_series_equal(result, expected)
