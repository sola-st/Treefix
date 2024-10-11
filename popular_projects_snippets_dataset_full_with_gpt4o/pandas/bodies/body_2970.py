# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# GH#18578
df = DataFrame(
    {
        0: date_range("2010", freq="D", periods=2, tz=tz),
        1: date_range("2010", freq="D", periods=2, tz=tz),
    }
)

result = df.diff(axis=1)
expected = DataFrame(
    {
        0: pd.TimedeltaIndex(["NaT", "NaT"]),
        1: pd.TimedeltaIndex(["0 days", "0 days"]),
    }
)
tm.assert_frame_equal(result, expected)
