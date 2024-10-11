# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_function.py
arr = pd.array([True, False, pd.NA], dtype="boolean")
result = arr.value_counts(dropna=False)
expected = pd.Series([1, 1, 1], index=arr, dtype="Int64")
assert expected.index.dtype == arr.dtype
tm.assert_series_equal(result, expected)

result = arr.value_counts(dropna=True)
expected = pd.Series([1, 1], index=arr[:-1], dtype="Int64")
assert expected.index.dtype == arr.dtype
tm.assert_series_equal(result, expected)
