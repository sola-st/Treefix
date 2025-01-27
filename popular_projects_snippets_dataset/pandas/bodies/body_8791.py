# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
if dtype.storage == "pyarrow":
    reason = (
        "unsupported operand type(s) for +: 'ArrowStringArray' and "
        "'ArrowStringArray'"
    )
    mark = pytest.mark.xfail(raises=NotImplementedError, reason=reason)
    request.node.add_marker(mark)

a = pd.Series(["a", "b", "c", None, None], dtype=dtype)
b = pd.Series(["x", "y", None, "z", None], dtype=dtype)

result = a + b
expected = pd.Series(["ax", "by", None, None, None], dtype=dtype)
tm.assert_series_equal(result, expected)

result = a.add(b)
tm.assert_series_equal(result, expected)

result = a.radd(b)
expected = pd.Series(["xa", "yb", None, None, None], dtype=dtype)
tm.assert_series_equal(result, expected)

result = a.add(b, fill_value="-")
expected = pd.Series(["ax", "by", "c-", "-z", None], dtype=dtype)
tm.assert_series_equal(result, expected)
