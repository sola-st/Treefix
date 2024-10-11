# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# GH#4533
df = DataFrame(
    {
        "time": [Timestamp("20130101 9:01"), Timestamp("20130101 9:02")],
        "value": [1.0, 2.0],
    }
)

res = df.diff()
exp = DataFrame(
    [[pd.NaT, np.nan], [pd.Timedelta("00:01:00"), 1]], columns=["time", "value"]
)
tm.assert_frame_equal(res, exp)
