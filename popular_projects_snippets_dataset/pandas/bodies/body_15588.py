# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# GH#13737
ser = Series([Period("2011-01", freq="M"), Period("NaT", freq="M")])

res = ser.fillna(Period("2012-01", freq="M"))
exp = Series([Period("2011-01", freq="M"), Period("2012-01", freq="M")])
tm.assert_series_equal(res, exp)
assert res.dtype == "Period[M]"
