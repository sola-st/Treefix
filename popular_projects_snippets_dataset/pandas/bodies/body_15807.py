# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
if dtype == "boolean" or (dtype == "timedelta64[ns]" and NaT in data):
    mark = pytest.mark.xfail(
        reason="TODO StringArray.astype() with missing values #GH40566"
    )
    request.node.add_marker(mark)
# GH-40351
ser = Series(data, dtype=dtype)

# Note: just passing .astype(dtype) fails for dtype="category"
#  with bc ser.dtype.categories will be object dtype whereas
#  result.dtype.categories will have string dtype
result = ser.astype(nullable_string_dtype).astype(ser.dtype)
tm.assert_series_equal(result, ser)
