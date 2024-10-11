# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# ufunc will not be boxed. Same test cases as the test_map_box
vals = [pd.Timestamp("2011-01-01"), pd.Timestamp("2011-01-02")]
s = Series(vals)
assert s.dtype == "datetime64[ns]"
# boxed value must be Timestamp instance
res = s.apply(lambda x: f"{type(x).__name__}_{x.day}_{x.tz}")
exp = Series(["Timestamp_1_None", "Timestamp_2_None"])
tm.assert_series_equal(res, exp)

vals = [
    pd.Timestamp("2011-01-01", tz="US/Eastern"),
    pd.Timestamp("2011-01-02", tz="US/Eastern"),
]
s = Series(vals)
assert s.dtype == "datetime64[ns, US/Eastern]"
res = s.apply(lambda x: f"{type(x).__name__}_{x.day}_{x.tz}")
exp = Series(["Timestamp_1_US/Eastern", "Timestamp_2_US/Eastern"])
tm.assert_series_equal(res, exp)

# timedelta
vals = [pd.Timedelta("1 days"), pd.Timedelta("2 days")]
s = Series(vals)
assert s.dtype == "timedelta64[ns]"
res = s.apply(lambda x: f"{type(x).__name__}_{x.days}")
exp = Series(["Timedelta_1", "Timedelta_2"])
tm.assert_series_equal(res, exp)

# period
vals = [pd.Period("2011-01-01", freq="M"), pd.Period("2011-01-02", freq="M")]
s = Series(vals)
assert s.dtype == "Period[M]"
res = s.apply(lambda x: f"{type(x).__name__}_{x.freqstr}")
exp = Series(["Period_M", "Period_M"])
tm.assert_series_equal(res, exp)
