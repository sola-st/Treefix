# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_between.py
ser = Series(bdate_range("1/1/2000", periods=20).astype(object))
ser[::2] = np.nan

result = ser[ser.between(ser[3], ser[17])]
expected = ser[3:18].dropna()
tm.assert_series_equal(result, expected)

result = ser[ser.between(ser[3], ser[17], inclusive="neither")]
expected = ser[5:16].dropna()
tm.assert_series_equal(result, expected)
