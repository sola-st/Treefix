# Extracted from ./data/repos/pandas/pandas/tests/strings/test_api.py
# https://github.com/pandas-dev/pandas/issues/10661

if any_string_dtype == "string[pyarrow]" or (
    any_string_dtype == "string" and get_option("string_storage") == "pyarrow"
):
    # unsupported operand type(s) for +: 'ArrowStringArray' and 'str'
    mark = pytest.mark.xfail(raises=NotImplementedError, reason="Not Implemented")
    request.node.add_marker(mark)

s = Series(list("aabb"), dtype=any_string_dtype)
s = s + " " + s
c = s.astype("category")
assert isinstance(c.str, strings.StringMethods)

method_name, args, kwargs = any_string_method

result = getattr(c.str, method_name)(*args, **kwargs)
expected = getattr(s.astype("object").str, method_name)(*args, **kwargs)

if isinstance(result, DataFrame):
    tm.assert_frame_equal(result, expected)
elif isinstance(result, Series):
    tm.assert_series_equal(result, expected)
else:
    # str.cat(others=None) returns string, for example
    assert result == expected
