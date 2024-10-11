# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
# GH 49473
ser = Series([1, 2, 3])
ser_orig = ser.copy()
ser2 = ser.set_axis(["a", "b", "c"], axis="index")

if using_copy_on_write:
    assert np.shares_memory(ser, ser2)
else:
    assert not np.shares_memory(ser, ser2)

# mutating ser triggers a copy-on-write for the column / block
ser2.iloc[0] = 0
assert not np.shares_memory(ser2, ser)
tm.assert_series_equal(ser, ser_orig)
