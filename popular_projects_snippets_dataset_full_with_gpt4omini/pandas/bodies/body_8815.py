# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
arr = pd.array(["a", "b", "a", pd.NA], dtype=dtype)
result = arr.value_counts(dropna=False)
expected = pd.Series([2, 1, 1], index=arr[[0, 1, 3]], dtype="Int64")
tm.assert_series_equal(result, expected)

result = arr.value_counts(dropna=True)
expected = pd.Series([2, 1], index=arr[:2], dtype="Int64")
tm.assert_series_equal(result, expected)
