# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_functions.py
ser = Series([1, 2], name="a")
ser2 = Series([3, 4], name="b")
expected = DataFrame({"a": [1, 2], "b": [3, 4]})
result = concat([ser, ser2], axis=1)

if using_copy_on_write:
    assert np.shares_memory(get_array(result, "a"), get_array(ser, "a"))
    assert np.shares_memory(get_array(result, "b"), get_array(ser2, "b"))
else:
    assert not np.shares_memory(get_array(result, "a"), get_array(ser, "a"))
    assert not np.shares_memory(get_array(result, "b"), get_array(ser2, "b"))

ser.iloc[0] = 100
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, "a"), get_array(ser, "a"))
    assert np.shares_memory(get_array(result, "b"), get_array(ser2, "b"))
tm.assert_frame_equal(result, expected)

ser2.iloc[0] = 1000
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, "b"), get_array(ser2, "b"))
tm.assert_frame_equal(result, expected)
