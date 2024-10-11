# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
df2 = DataFrame(
    {
        "A": Timestamp("20130102", tz="US/Eastern"),
        "B": Timestamp("20130603", tz="CET"),
    },
    index=range(5),
)

# concat
df3 = concat([df2.A.to_frame(), df2.B.to_frame()], axis=1)
tm.assert_frame_equal(df2, df3)
