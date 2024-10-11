# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_astype.py
# astype to BooleanArray
arr = pd.array([0.0, 1.0, None], dtype="Float64")

result = arr.astype("boolean")
expected = pd.array([False, True, None], dtype="boolean")
tm.assert_extension_array_equal(result, expected)
result = arr.astype(pd.BooleanDtype())
tm.assert_extension_array_equal(result, expected)
