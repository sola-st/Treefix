# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
expected = Series([True, True, False, False, False])

ser = Series(date_range("jan-01-2013", "jan-05-2013"))

dta = ser[:2]._values.astype("M8[s]")
result = ser.isin(list(dta))
tm.assert_series_equal(result, expected)
