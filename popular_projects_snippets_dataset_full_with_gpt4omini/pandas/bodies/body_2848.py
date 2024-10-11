# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# with datelike
# GH#6344
df = DataFrame(
    {
        "Date": [NaT, Timestamp("2014-1-1")],
        "Date2": [Timestamp("2013-1-1"), NaT],
    }
)

expected = df.copy()
expected["Date"] = expected["Date"].fillna(df.loc[df.index[0], "Date2"])
result = df.fillna(value={"Date": df["Date2"]})
tm.assert_frame_equal(result, expected)
