# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# with timezone
# GH#15855
df = DataFrame({"A": [Timestamp("2012-11-11 00:00:00+01:00"), NaT]})
exp = DataFrame(
    {
        "A": [
            Timestamp("2012-11-11 00:00:00+01:00"),
            Timestamp("2012-11-11 00:00:00+01:00"),
        ]
    }
)
tm.assert_frame_equal(df.fillna(method="pad"), exp)

df = DataFrame({"A": [NaT, Timestamp("2012-11-11 00:00:00+01:00")]})
exp = DataFrame(
    {
        "A": [
            Timestamp("2012-11-11 00:00:00+01:00"),
            Timestamp("2012-11-11 00:00:00+01:00"),
        ]
    }
)
tm.assert_frame_equal(df.fillna(method="bfill"), exp)
