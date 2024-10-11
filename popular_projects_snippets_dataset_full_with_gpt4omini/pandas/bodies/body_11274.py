# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH 8542
# length=2
df = DataFrame(
    {"event": ["start", "start"], "change": [1234, 5678]},
    index=pd.DatetimeIndex(["2014-09-10", "2013-10-10"]),
)
grouped = df.groupby([Grouper(freq="M"), "event"])
assert len(grouped.groups) == 2
assert grouped.ngroups == 2
assert (Timestamp("2014-09-30"), "start") in grouped.groups
assert (Timestamp("2013-10-31"), "start") in grouped.groups

res = grouped.get_group((Timestamp("2014-09-30"), "start"))
tm.assert_frame_equal(res, df.iloc[[0], :])
res = grouped.get_group((Timestamp("2013-10-31"), "start"))
tm.assert_frame_equal(res, df.iloc[[1], :])

df = DataFrame(
    {"event": ["start", "start", "start"], "change": [1234, 5678, 9123]},
    index=pd.DatetimeIndex(["2014-09-10", "2013-10-10", "2014-09-15"]),
)
grouped = df.groupby([Grouper(freq="M"), "event"])
assert len(grouped.groups) == 2
assert grouped.ngroups == 2
assert (Timestamp("2014-09-30"), "start") in grouped.groups
assert (Timestamp("2013-10-31"), "start") in grouped.groups

res = grouped.get_group((Timestamp("2014-09-30"), "start"))
tm.assert_frame_equal(res, df.iloc[[0, 2], :])
res = grouped.get_group((Timestamp("2013-10-31"), "start"))
tm.assert_frame_equal(res, df.iloc[[1], :])

# length=3
df = DataFrame(
    {"event": ["start", "start", "start"], "change": [1234, 5678, 9123]},
    index=pd.DatetimeIndex(["2014-09-10", "2013-10-10", "2014-08-05"]),
)
grouped = df.groupby([Grouper(freq="M"), "event"])
assert len(grouped.groups) == 3
assert grouped.ngroups == 3
assert (Timestamp("2014-09-30"), "start") in grouped.groups
assert (Timestamp("2013-10-31"), "start") in grouped.groups
assert (Timestamp("2014-08-31"), "start") in grouped.groups

res = grouped.get_group((Timestamp("2014-09-30"), "start"))
tm.assert_frame_equal(res, df.iloc[[0], :])
res = grouped.get_group((Timestamp("2013-10-31"), "start"))
tm.assert_frame_equal(res, df.iloc[[1], :])
res = grouped.get_group((Timestamp("2014-08-31"), "start"))
tm.assert_frame_equal(res, df.iloc[[2], :])
