# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
if dtype.storage == "pyarrow" and (pa_version_under6p0 or box is pd.array):
    if box is pd.array:
        reason = "'<=' not supported between instances of 'str' and 'NoneType'"
    else:
        reason = "'ArrowStringArray' object has no attribute 'max'"
    mark = pytest.mark.xfail(raises=TypeError, reason=reason)
    request.node.add_marker(mark)

arr = box(["a", "b", "c", None], dtype=dtype)
result = getattr(np, method)(arr)
expected = "a" if method == "min" else "c"
assert result == expected
