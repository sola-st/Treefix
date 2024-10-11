# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_astype.py
# astype to IntegerArray
arr = pd.array([0.0, 1.5, None], dtype="Float64")

result = arr.astype("Int64")
expected = pd.array([0, 1, None], dtype="Int64")
tm.assert_extension_array_equal(result, expected)
