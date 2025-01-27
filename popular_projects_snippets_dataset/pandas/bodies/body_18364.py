# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
box = box_with_array
xbox = np.ndarray if box is pd.array else box

ser = Series([Timedelta(days=59)] * 3)
ser[2] = np.nan
flat = ser
ser = tm.box_expected(ser, box)

# op
expected = Series([x / np.timedelta64(m, unit) for x in flat])
expected = tm.box_expected(expected, xbox)
result = ser / np.timedelta64(m, unit)
tm.assert_equal(result, expected)

# reverse op
expected = Series([Timedelta(np.timedelta64(m, unit)) / x for x in flat])
expected = tm.box_expected(expected, xbox)
result = np.timedelta64(m, unit) / ser
tm.assert_equal(result, expected)
