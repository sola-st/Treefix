# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_astype.py
# astype to FloatingArray
arr = pd.array([0.0, 1.0, None], dtype="Float64")

result = arr.astype("Float64")
tm.assert_extension_array_equal(result, arr)
result = arr.astype(pd.Float64Dtype())
tm.assert_extension_array_equal(result, arr)
result = arr.astype("Float32")
expected = pd.array([0.0, 1.0, None], dtype="Float32")
tm.assert_extension_array_equal(result, expected)
