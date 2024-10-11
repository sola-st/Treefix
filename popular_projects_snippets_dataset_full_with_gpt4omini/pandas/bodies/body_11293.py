# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_functions.py
ser = Series([1, 2], name="a")
ser2 = Series([3, 4], name="b")
ser_orig = ser.copy()
ser2_orig = ser2.copy()
result = concat([ser, ser2], axis=1)

if using_copy_on_write:
    assert np.shares_memory(get_array(result, "a"), ser.values)
    assert np.shares_memory(get_array(result, "b"), ser2.values)
else:
    assert not np.shares_memory(get_array(result, "a"), ser.values)
    assert not np.shares_memory(get_array(result, "b"), ser2.values)

result.iloc[0, 0] = 100
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, "a"), ser.values)
    assert np.shares_memory(get_array(result, "b"), ser2.values)

result.iloc[0, 1] = 1000
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, "b"), ser2.values)
tm.assert_series_equal(ser, ser_orig)
tm.assert_series_equal(ser2, ser2_orig)
