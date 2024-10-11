# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# see GH#9757

td = Series([Timedelta(1, unit="d")])
ser = td.astype(str)

expected = Series(["1 days"])
tm.assert_series_equal(ser, expected)
