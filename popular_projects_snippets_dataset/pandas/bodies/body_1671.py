# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
a = array(arg, dtype="Int64")
result = safe_sort(a)
expected = array(exp, dtype="Int64")
tm.assert_extension_array_equal(result, expected)
