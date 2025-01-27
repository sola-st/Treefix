# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append_common.py
# GH 13221
# different datetimelike
pi1 = pd.PeriodIndex(["2011-01", "2011-02"], freq="M")
tdi = pd.TimedeltaIndex(["1 days", "2 days"])
exp = Index(
    [
        pd.Period("2011-01", freq="M"),
        pd.Period("2011-02", freq="M"),
        pd.Timedelta("1 days"),
        pd.Timedelta("2 days"),
    ],
    dtype=object,
)

res = pi1.append(tdi)
tm.assert_index_equal(res, exp)

ps1 = Series(pi1)
tds = Series(tdi)
res = ps1._append(tds)
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))

res = pd.concat([ps1, tds])
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))

# inverse
exp = Index(
    [
        pd.Timedelta("1 days"),
        pd.Timedelta("2 days"),
        pd.Period("2011-01", freq="M"),
        pd.Period("2011-02", freq="M"),
    ],
    dtype=object,
)

res = tdi.append(pi1)
tm.assert_index_equal(res, exp)

ps1 = Series(pi1)
tds = Series(tdi)
res = tds._append(ps1)
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))

res = pd.concat([tds, ps1])
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
