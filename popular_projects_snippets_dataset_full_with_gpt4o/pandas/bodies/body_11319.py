# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
ser = Series([1, 2])
ser_orig = ser.copy()
ser_other = ser.copy()
ser2, ser_other_result = ser.align(ser_other)

if using_copy_on_write:
    assert np.shares_memory(ser2.values, ser.values)
    assert np.shares_memory(ser_other_result.values, ser_other.values)
else:
    assert not np.shares_memory(ser2.values, ser.values)
    assert not np.shares_memory(ser_other_result.values, ser_other.values)

ser2.iloc[0] = 0
ser_other_result.iloc[0] = 0
if using_copy_on_write:
    assert not np.shares_memory(ser2.values, ser.values)
    assert not np.shares_memory(ser_other_result.values, ser_other.values)
tm.assert_series_equal(ser, ser_orig)
tm.assert_series_equal(ser_other, ser_orig)
