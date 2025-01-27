# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# GH#1430
periods = 1000
ind = date_range(start="2012/1/1", freq="5min", periods=periods)
df = DataFrame(
    {"high": np.arange(periods), "low": np.arange(periods)}, index=ind
)
grouped = df.groupby(lambda x: datetime(x.year, x.month, x.day))

# it works!
groups = grouped.groups
assert isinstance(list(groups.keys())[0], datetime)

# GH#11442
index = date_range("2015/01/01", periods=5, name="date")
df = DataFrame({"A": [5, 6, 7, 8, 9], "B": [1, 2, 3, 4, 5]}, index=index)
result = df.groupby(level="date").groups
dates = ["2015-01-05", "2015-01-04", "2015-01-03", "2015-01-02", "2015-01-01"]
expected = {
    Timestamp(date): DatetimeIndex([date], name="date") for date in dates
}
tm.assert_dict_equal(result, expected)

grouped = df.groupby(level="date")
for date in dates:
    result = grouped.get_group(date)
    data = [[df.loc[date, "A"], df.loc[date, "B"]]]
    expected_index = DatetimeIndex([date], name="date", freq="D")
    expected = DataFrame(data, columns=list("AB"), index=expected_index)
    tm.assert_frame_equal(result, expected)
