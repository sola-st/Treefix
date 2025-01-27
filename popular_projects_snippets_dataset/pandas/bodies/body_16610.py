# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# GH 14844
left = pd.DataFrame(
    {
        "date": pd.date_range(
            start=to_datetime("2016-01-02"),
            freq="D",
            periods=5,
            tz=pytz.timezone("UTC"),
        ),
        "value1": np.arange(5),
    }
)
right = pd.DataFrame(
    {
        "date": pd.date_range(
            start=to_datetime("2016-01-01"),
            freq="D",
            periods=5,
            tz=pytz.timezone("UTC"),
        ),
        "value2": list("ABCDE"),
    }
)
result = merge_asof(left, right, on="date", tolerance=Timedelta("1 day"))

expected = pd.DataFrame(
    {
        "date": pd.date_range(
            start=to_datetime("2016-01-02"),
            freq="D",
            periods=5,
            tz=pytz.timezone("UTC"),
        ),
        "value1": np.arange(5),
        "value2": list("BCDEE"),
    }
)
tm.assert_frame_equal(result, expected)
