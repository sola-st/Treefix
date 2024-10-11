# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# GH#10442 : testing astype(str) is correct for Series/DatetimeIndex
dti = date_range("2012-01-01", periods=3)
result = Series(dti).astype(str)
expected = Series(["2012-01-01", "2012-01-02", "2012-01-03"], dtype=object)
tm.assert_series_equal(result, expected)
