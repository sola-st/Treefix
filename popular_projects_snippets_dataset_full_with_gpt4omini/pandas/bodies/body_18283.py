# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
# GH#22378
# Check that scalars satisfying is_extension_array_dtype(obj)
# do not incorrectly try to dispatch to an ExtensionArray operation

arr = Series(["a", "b", "c"])
expected = Series([op(x, other) for x in arr])

arr = tm.box_expected(arr, box_with_array)
expected = tm.box_expected(expected, box_with_array)

result = op(arr, other)
tm.assert_equal(result, expected)
