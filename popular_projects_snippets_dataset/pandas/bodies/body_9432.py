# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_function.py
arr = pd.array([1, 2, 1, pd.NA], dtype="Int64")
result = arr.value_counts(dropna=False)
ex_index = pd.Index([1, 2, pd.NA], dtype="Int64")
assert ex_index.dtype == "Int64"
expected = pd.Series([2, 1, 1], index=ex_index, dtype="Int64")
tm.assert_series_equal(result, expected)

result = arr.value_counts(dropna=True)
expected = pd.Series([2, 1], index=arr[:2], dtype="Int64")
assert expected.index.dtype == arr.dtype
tm.assert_series_equal(result, expected)
