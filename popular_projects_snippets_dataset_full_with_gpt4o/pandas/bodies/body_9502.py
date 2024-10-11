# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_ops.py
# matching numpy behavior, abs is the identity function
arr = pd.array([True, False, None], dtype="boolean")
result = abs(arr)

tm.assert_extension_array_equal(result, arr)
