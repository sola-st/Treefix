# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
if dtype.storage == "pyarrow":
    reason = "unsupported operand type(s) for +: 'ArrowStringArray' and 'list'"
    mark = pytest.mark.xfail(raises=NotImplementedError, reason=reason)
    request.node.add_marker(mark)

a = pd.array(["a", "b", None, None], dtype=dtype)
other = ["x", None, "y", None]

result = a + other
expected = pd.array(["ax", None, None, None], dtype=dtype)
tm.assert_extension_array_equal(result, expected)

result = other + a
expected = pd.array(["xa", None, None, None], dtype=dtype)
tm.assert_extension_array_equal(result, expected)
