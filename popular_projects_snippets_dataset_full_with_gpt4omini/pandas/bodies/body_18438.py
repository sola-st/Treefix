# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
ser = date_range("2014-03-17", periods=2, freq="D", tz="US/Eastern")
ser = ser._with_freq(None)
ts = ser[0]

ser = tm.box_expected(ser, box_with_array)

delta_series = Series([np.timedelta64(0, "D"), np.timedelta64(1, "D")])
expected = tm.box_expected(delta_series, box_with_array)

tm.assert_equal(ser - ts, expected)
tm.assert_equal(ts - ser, -expected)
