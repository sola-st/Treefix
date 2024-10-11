# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_astype.py
# astype to IntegerArray
arr = pd.array([True, False, None], dtype="boolean")

result = arr.astype("Int64")
expected = pd.array([1, 0, None], dtype="Int64")
tm.assert_extension_array_equal(result, expected)
