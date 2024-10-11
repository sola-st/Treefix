# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dtypes.py
df = DataFrame(
    {
        "A": Series(date_range("2012-1-1", periods=3, freq="D")),
        "B": Series([timedelta(days=i) for i in range(3)]),
    }
)
result = df.dtypes
expected = Series(
    [np.dtype("datetime64[ns]"), np.dtype("timedelta64[ns]")], index=list("AB")
)
tm.assert_series_equal(result, expected)

df["C"] = df["A"] + df["B"]
result = df.dtypes
expected = Series(
    [
        np.dtype("datetime64[ns]"),
        np.dtype("timedelta64[ns]"),
        np.dtype("datetime64[ns]"),
    ],
    index=list("ABC"),
)
tm.assert_series_equal(result, expected)

# mixed int types
df["D"] = 1
result = df.dtypes
expected = Series(
    [
        np.dtype("datetime64[ns]"),
        np.dtype("timedelta64[ns]"),
        np.dtype("datetime64[ns]"),
        np.dtype("int64"),
    ],
    index=list("ABCD"),
)
tm.assert_series_equal(result, expected)
