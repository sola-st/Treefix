# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_take.py
ser = Series([-1, 5, 6, 2, 4])

actual = ser.take([1, 3, 4])
expected = Series([5, 2, 4], index=[1, 3, 4])
tm.assert_series_equal(actual, expected)

actual = ser.take([-1, 3, 4])
expected = Series([4, 2, 4], index=[4, 3, 4])
tm.assert_series_equal(actual, expected)

msg = lambda x: f"index {x} is out of bounds for( axis 0 with)? size 5"
with pytest.raises(IndexError, match=msg(10)):
    ser.take([1, 10])
with pytest.raises(IndexError, match=msg(5)):
    ser.take([2, 5])
