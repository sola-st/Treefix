# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_select_dtypes.py

df2 = DataFrame(
    {
        "A": Timestamp("20130102", tz="US/Eastern"),
        "B": Timestamp("20130603", tz="CET"),
    },
    index=range(5),
)
df3 = pd.concat([df2.A.to_frame(), df2.B.to_frame()], axis=1)
result = df3.select_dtypes(include=["datetime64[ns]"])
expected = df3.reindex(columns=[])
tm.assert_frame_equal(result, expected)
