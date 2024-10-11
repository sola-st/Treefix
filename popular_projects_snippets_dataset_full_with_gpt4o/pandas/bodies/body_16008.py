# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
# GH#36621 dont cast integers to datetimes for isin
dti = date_range("2013-01-01", "2013-01-05")
ser = Series(dti)

comps = np.asarray([1356998400000000000], dtype=dtype)

res = dti.isin(comps)
expected = np.array([False] * len(dti), dtype=bool)
tm.assert_numpy_array_equal(res, expected)

res = ser.isin(comps)
tm.assert_series_equal(res, Series(expected))

res = pd.core.algorithms.isin(ser, comps)
tm.assert_numpy_array_equal(res, expected)
