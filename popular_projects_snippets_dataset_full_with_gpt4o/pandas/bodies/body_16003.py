# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
expected = Series([True, True, False, False, False])

ser = Series(date_range("jan-01-2013", "jan-05-2013"))

# fails on dtype conversion in the first place
day_values = np.asarray(ser[0:2].values).astype("datetime64[D]")
result = ser.isin(day_values)
tm.assert_series_equal(result, expected)

dta = ser[:2]._values.astype("M8[s]")
result = ser.isin(dta)
tm.assert_series_equal(result, expected)
