# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_function.py
ser = pd.Series([], dtype="Float64")
result = ser.value_counts()
idx = pd.Index([], dtype="Float64")
assert idx.dtype == "Float64"
expected = pd.Series([], index=idx, dtype="Int64")
tm.assert_series_equal(result, expected)
