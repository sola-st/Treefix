# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py

op_name = f"__{comparison_op.__name__}__"

a = pd.array(["a", None, "c"], dtype=dtype)
other = [None, None, "c"]
result = getattr(a, op_name)(other)
expected = np.empty_like(a, dtype="object")
expected[-1] = getattr(other[-1], op_name)(a[-1])
expected = pd.array(expected, dtype="boolean")
tm.assert_extension_array_equal(result, expected)

result = getattr(a, op_name)(pd.NA)
expected = pd.array([None, None, None], dtype="boolean")
tm.assert_extension_array_equal(result, expected)
