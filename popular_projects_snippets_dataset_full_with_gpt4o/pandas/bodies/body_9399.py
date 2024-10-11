# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_dtypes.py
arr = pd.array([1, 2, None], dtype="Int64")
result = arr.astype("Float64")
expected = pd.array([1.0, 2.0, None], dtype="Float64")
tm.assert_extension_array_equal(result, expected)
