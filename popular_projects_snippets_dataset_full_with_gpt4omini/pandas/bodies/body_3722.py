# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_describe.py
# GH#6145
t1 = pd.timedelta_range("1 days", freq="D", periods=5)
t2 = pd.timedelta_range("1 hours", freq="H", periods=5)
df = DataFrame({"t1": t1, "t2": t2})

expected = DataFrame(
    {
        "t1": [
            5,
            pd.Timedelta("3 days"),
            df.iloc[:, 0].std(),
            pd.Timedelta("1 days"),
            pd.Timedelta("2 days"),
            pd.Timedelta("3 days"),
            pd.Timedelta("4 days"),
            pd.Timedelta("5 days"),
        ],
        "t2": [
            5,
            pd.Timedelta("3 hours"),
            df.iloc[:, 1].std(),
            pd.Timedelta("1 hours"),
            pd.Timedelta("2 hours"),
            pd.Timedelta("3 hours"),
            pd.Timedelta("4 hours"),
            pd.Timedelta("5 hours"),
        ],
    },
    index=["count", "mean", "std", "min", "25%", "50%", "75%", "max"],
)

result = df.describe()
tm.assert_frame_equal(result, expected)

exp_repr = (
    "                              t1                         t2\n"
    "count                          5                          5\n"
    "mean             3 days 00:00:00            0 days 03:00:00\n"
    "std    1 days 13:56:50.394919273  0 days 01:34:52.099788303\n"
    "min              1 days 00:00:00            0 days 01:00:00\n"
    "25%              2 days 00:00:00            0 days 02:00:00\n"
    "50%              3 days 00:00:00            0 days 03:00:00\n"
    "75%              4 days 00:00:00            0 days 04:00:00\n"
    "max              5 days 00:00:00            0 days 05:00:00"
)
assert repr(result) == exp_repr
