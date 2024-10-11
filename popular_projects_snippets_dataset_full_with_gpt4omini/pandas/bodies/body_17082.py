# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append_common.py
# GH 13626
# result must be Timestamp/Timedelta, not datetime.datetime/timedelta
dti = pd.DatetimeIndex(["2011-01-01", "2011-01-02"])
tdi = pd.TimedeltaIndex(["1 days", "2 days"])

exp = Index(
    [
        pd.Timestamp("2011-01-01"),
        pd.Timestamp("2011-01-02"),
        pd.Timedelta("1 days"),
        pd.Timedelta("2 days"),
    ]
)

res = dti.append(tdi)
tm.assert_index_equal(res, exp)
assert isinstance(res[0], pd.Timestamp)
assert isinstance(res[-1], pd.Timedelta)

dts = Series(dti)
tds = Series(tdi)
res = dts._append(tds)
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
assert isinstance(res.iloc[0], pd.Timestamp)
assert isinstance(res.iloc[-1], pd.Timedelta)

res = pd.concat([dts, tds])
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
assert isinstance(res.iloc[0], pd.Timestamp)
assert isinstance(res.iloc[-1], pd.Timedelta)
