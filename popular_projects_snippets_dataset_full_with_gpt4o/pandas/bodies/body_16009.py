# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
dti = date_range("2013-01-01", "2013-01-05")
ser = Series(dti)

other = dti.tz_localize("UTC")

res = dti.isin(other)
expected = np.array([False] * len(dti), dtype=bool)
tm.assert_numpy_array_equal(res, expected)

res = ser.isin(other)
tm.assert_series_equal(res, Series(expected))

res = pd.core.algorithms.isin(ser, other)
tm.assert_numpy_array_equal(res, expected)
