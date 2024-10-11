# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# GH 13709
df1 = pd.DataFrame(
    {
        "time": to_datetime(
            ["2016-07-15 13:30:00.030", "2016-07-15 13:30:00.030"]
        ),
        "username": ["bob", "charlie"],
    }
)
df2 = pd.DataFrame(
    {
        "time": to_datetime(
            ["2016-07-15 13:30:00.000", "2016-07-15 13:30:00.030"]
        ),
        "version": [1, 2],
    }
)

result = merge_asof(
    df1,
    df2,
    on="time",
    allow_exact_matches=False,
    tolerance=Timedelta("10ms"),
)
expected = pd.DataFrame(
    {
        "time": to_datetime(
            ["2016-07-15 13:30:00.030", "2016-07-15 13:30:00.030"]
        ),
        "username": ["bob", "charlie"],
        "version": [np.nan, np.nan],
    }
)
tm.assert_frame_equal(result, expected)
