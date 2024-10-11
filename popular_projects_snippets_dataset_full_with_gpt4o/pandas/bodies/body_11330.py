# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
ser = Series([1, val, 4])
ser_orig = ser.copy()
ser2 = ser.dropna()

if using_copy_on_write:
    assert np.shares_memory(ser2.values, ser.values)
else:
    assert not np.shares_memory(ser2.values, ser.values)

ser2.iloc[0] = 0
if using_copy_on_write:
    assert not np.shares_memory(ser2.values, ser.values)
tm.assert_series_equal(ser, ser_orig)
