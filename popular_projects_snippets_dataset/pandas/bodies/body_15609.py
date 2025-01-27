# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
ser = Series(np.random.randint(-100, 100, 50))
return_value = ser.fillna(method="ffill", inplace=True)
assert return_value is None
tm.assert_series_equal(ser.fillna(method="ffill", inplace=False), ser)
