# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_copy.py
# GH#11794
# copy of tz-aware
expected = Series([Timestamp("2012/01/01", tz="UTC")])
expected2 = Series([Timestamp("1999/01/01", tz="UTC")])

ser = Series([Timestamp("2012/01/01", tz="UTC")])

if deep == "default":
    ser2 = ser.copy()
else:
    ser2 = ser.copy(deep=deep)

if using_copy_on_write:
    # INFO(CoW) a shallow copy doesn't yet copy the data
    # but parent will not be modified (CoW)
    if deep is None or deep is False:
        assert np.may_share_memory(ser.values, ser2.values)
    else:
        assert not np.may_share_memory(ser.values, ser2.values)

ser2[0] = Timestamp("1999/01/01", tz="UTC")

# default deep is True
if deep is not False or using_copy_on_write:
    # Did not modify original Series
    tm.assert_series_equal(ser2, expected2)
    tm.assert_series_equal(ser, expected)
else:
    # we DID modify the original Series
    tm.assert_series_equal(ser2, expected2)
    tm.assert_series_equal(ser, expected2)
