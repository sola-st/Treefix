# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_astype.py
# astype to BooleanArray
arr = pd.array([True, False, None], dtype="boolean")

result = arr.astype("boolean")
tm.assert_extension_array_equal(result, arr)
result = arr.astype(pd.BooleanDtype())
tm.assert_extension_array_equal(result, arr)
