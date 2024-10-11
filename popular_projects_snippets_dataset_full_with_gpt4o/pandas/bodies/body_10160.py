# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 35486
df = DataFrame(
    {"a": [1, 2, 3, 2], "b": [4.0, 2.0, 3.0, 1.0], "c": [10, 20, 30, 20]}
)
result = df.groupby("a")[["b"]].rolling(2).max()
expected = DataFrame(
    [np.nan, np.nan, 2.0, np.nan],
    columns=["b"],
    index=MultiIndex.from_tuples(
        ((1, 0), (2, 1), (2, 3), (3, 2)), names=["a", None]
    ),
)
tm.assert_frame_equal(result, expected)

result = df.groupby("a")["b"].rolling(2).max()
expected = Series(
    [np.nan, np.nan, 2.0, np.nan],
    index=MultiIndex.from_tuples(
        ((1, 0), (2, 1), (2, 3), (3, 2)), names=["a", None]
    ),
    name="b",
)
tm.assert_series_equal(result, expected)
