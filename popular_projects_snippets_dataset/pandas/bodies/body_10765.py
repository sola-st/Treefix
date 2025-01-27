# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# GH#42659
df = DataFrame(
    {
        "a": [1, 1, 2, 2],
        "b": [pd.Timedelta("1d"), pd.Timedelta("2d"), pd.Timedelta("3d"), pd.NaT],
    }
)
td3 = pd.Timedelta(days=3)

gb = df.groupby("a")

res = gb.sum()
expected = DataFrame({"b": [td3, td3]}, index=Index([1, 2], name="a"))
tm.assert_frame_equal(res, expected)

res = gb["b"].sum()
tm.assert_series_equal(res, expected["b"])

res = gb["b"].sum(min_count=2)
expected = Series([td3, pd.NaT], dtype="m8[ns]", name="b", index=expected.index)
tm.assert_series_equal(res, expected)
