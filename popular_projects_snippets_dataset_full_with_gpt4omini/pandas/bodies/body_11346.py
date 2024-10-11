# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
ser = Series([1, 2, 3])
ser_orig = ser.copy()
ser2 = ser.set_flags(allows_duplicate_labels=False)

assert np.shares_memory(ser, ser2)

# mutating ser triggers a copy-on-write for the column / block
ser2.iloc[0] = 0
if using_copy_on_write:
    assert not np.shares_memory(ser2, ser)
    tm.assert_series_equal(ser, ser_orig)
else:
    assert np.shares_memory(ser2, ser)
    expected = Series([0, 2, 3])
    tm.assert_series_equal(ser, expected)
