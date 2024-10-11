# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
if dtype.storage == "pyarrow" and pa_version_under6p0:
    reason = "'ArrowStringArray' object has no attribute 'max'"
    mark = pytest.mark.xfail(raises=TypeError, reason=reason)
    request.node.add_marker(mark)

arr = pd.Series(["a", "b", "c", None], dtype=dtype)
result = getattr(arr, method)(skipna=skipna)
if skipna:
    expected = "a" if method == "min" else "c"
    assert result == expected
else:
    assert result is pd.NA
