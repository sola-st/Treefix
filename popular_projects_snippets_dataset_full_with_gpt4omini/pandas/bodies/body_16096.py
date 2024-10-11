# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH 19468
dti = DatetimeIndex(["20171111", "20181212"]).repeat(2)
ser = Series(pd.Categorical(dti), name="foo")
result = ser.dt.year
expected = Series([2017, 2017, 2018, 2018], dtype="int32", name="foo")
tm.assert_series_equal(result, expected)
