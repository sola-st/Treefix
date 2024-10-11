# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# GH#48863
df = DataFrame(
    {
        "date1": to_datetime(["2018-05-30", None]),
        "date2": to_datetime(["2018-09-30", None]),
    }
)
expected = df.copy()
df.fillna(np.nan, inplace=True)
tm.assert_frame_equal(df, expected)
