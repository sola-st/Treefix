# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# naive shift
ser = datetime_frame["A"]

shifted = datetime_frame.shift(5)
tm.assert_index_equal(shifted.index, datetime_frame.index)

shifted_ser = ser.shift(5)
tm.assert_series_equal(shifted["A"], shifted_ser)

shifted = datetime_frame.shift(-5)
tm.assert_index_equal(shifted.index, datetime_frame.index)

shifted_ser = ser.shift(-5)
tm.assert_series_equal(shifted["A"], shifted_ser)

unshifted = datetime_frame.shift(5).shift(-5)
tm.assert_numpy_array_equal(
    unshifted.dropna().values, datetime_frame.values[:-5]
)

unshifted_ser = ser.shift(5).shift(-5)
tm.assert_numpy_array_equal(unshifted_ser.dropna().values, ser.values[:-5])
