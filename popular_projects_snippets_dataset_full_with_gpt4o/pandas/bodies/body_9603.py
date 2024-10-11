# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_function.py
arr = pd.array([0.1, 0.2, 0.1, pd.NA], dtype="Float64")
result = arr.value_counts(dropna=False)
idx = pd.Index([0.1, 0.2, pd.NA], dtype=arr.dtype)
assert idx.dtype == arr.dtype
expected = pd.Series([2, 1, 1], index=idx, dtype="Int64")
tm.assert_series_equal(result, expected)

result = arr.value_counts(dropna=True)
expected = pd.Series([2, 1], index=idx[:-1], dtype="Int64")
tm.assert_series_equal(result, expected)
