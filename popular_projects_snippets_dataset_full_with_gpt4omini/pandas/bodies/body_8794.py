# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
if dtype.storage == "pyarrow":
    reason = "unsupported operand type(s) for *: 'ArrowStringArray' and 'int'"
    mark = pytest.mark.xfail(raises=NotImplementedError, reason=reason)
    request.node.add_marker(mark)

a = pd.array(["a", "b", None], dtype=dtype)
result = a * 2
expected = pd.array(["aa", "bb", None], dtype=dtype)
tm.assert_extension_array_equal(result, expected)

result = 2 * a
tm.assert_extension_array_equal(result, expected)
