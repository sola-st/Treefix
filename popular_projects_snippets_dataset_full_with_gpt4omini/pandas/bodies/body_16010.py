# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
dti = date_range("2013-01-01", "2013-01-05")
pi = dti.to_period("M")
ser = Series(pi)

# We construct another PeriodIndex with the same i8 values
#  but different dtype
dtype = dti.to_period("Y").dtype
other = PeriodArray._simple_new(pi.asi8, dtype=dtype)

res = pi.isin(other)
expected = np.array([False] * len(pi), dtype=bool)
tm.assert_numpy_array_equal(res, expected)

res = ser.isin(other)
tm.assert_series_equal(res, Series(expected))

res = pd.core.algorithms.isin(ser, other)
tm.assert_numpy_array_equal(res, expected)
