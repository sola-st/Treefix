# Extracted from ./data/repos/pandas/pandas/tests/series/test_logical_ops.py
# boolean &, |, ^ should work with object arrays and propagate NAs
ser = Series(bdate_range("1/1/2000", periods=10), dtype=object)
ser[::2] = np.nan

mask = ser.isna()
filled = ser.fillna(ser[0])

result = bool_op(ser < ser[9], ser > ser[3])

expected = bool_op(filled < filled[9], filled > filled[3])
expected[mask] = False
tm.assert_series_equal(result, expected)
