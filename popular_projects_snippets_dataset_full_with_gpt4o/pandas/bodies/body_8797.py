# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
op_name = f"__{comparison_op.__name__}__"
a = pd.array(["a", None, "c"], dtype=dtype)
other = "a"
result = getattr(a, op_name)(other)
expected = np.array([getattr(item, op_name)(other) for item in a], dtype=object)
expected = pd.array(expected, dtype="boolean")
tm.assert_extension_array_equal(result, expected)
