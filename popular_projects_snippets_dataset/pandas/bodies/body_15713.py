# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_copy.py

ser = Series(np.arange(10), dtype="float64")

# default deep is True
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

ser2[::2] = np.NaN

if deep is not False or using_copy_on_write:
    # Did not modify original Series
    assert np.isnan(ser2[0])
    assert not np.isnan(ser[0])
else:
    # we DID modify the original Series
    assert np.isnan(ser2[0])
    assert np.isnan(ser[0])
