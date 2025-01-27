# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# Test constructing with a datetimetz dtype
# .values produces numpy datetimes, so these are considered naive
# .asi8 produces integers, so these are considered epoch timestamps
# ^the above will be true in a later version. Right now we `.view`
# the i8 values as NS_DTYPE, effectively treating them as wall times.
index = date_range("2011-01-01", periods=5)
arg = getattr(index, attr)
index = index.tz_localize(tz_naive_fixture)
dtype = index.dtype

# As of 2.0 astype raises on dt64.astype(dt64tz)
err = tz_naive_fixture is not None
msg = "Cannot use .astype to convert from timezone-naive dtype to"

if attr == "asi8":
    result = DatetimeIndex(arg).tz_localize(tz_naive_fixture)
    tm.assert_index_equal(result, index)
elif klass is Index:
    with pytest.raises(TypeError, match="unexpected keyword"):
        klass(arg, tz=tz_naive_fixture)
else:
    result = klass(arg, tz=tz_naive_fixture)
    tm.assert_index_equal(result, index)

if attr == "asi8":
    if err:
        with pytest.raises(TypeError, match=msg):
            DatetimeIndex(arg).astype(dtype)
    else:
        result = DatetimeIndex(arg).astype(dtype)
        tm.assert_index_equal(result, index)
else:
    result = klass(arg, dtype=dtype)
    tm.assert_index_equal(result, index)

if attr == "asi8":
    result = DatetimeIndex(list(arg)).tz_localize(tz_naive_fixture)
    tm.assert_index_equal(result, index)
elif klass is Index:
    with pytest.raises(TypeError, match="unexpected keyword"):
        klass(arg, tz=tz_naive_fixture)
else:
    result = klass(list(arg), tz=tz_naive_fixture)
    tm.assert_index_equal(result, index)

if attr == "asi8":
    if err:
        with pytest.raises(TypeError, match=msg):
            DatetimeIndex(list(arg)).astype(dtype)
    else:
        result = DatetimeIndex(list(arg)).astype(dtype)
        tm.assert_index_equal(result, index)
else:
    result = klass(list(arg), dtype=dtype)
    tm.assert_index_equal(result, index)
