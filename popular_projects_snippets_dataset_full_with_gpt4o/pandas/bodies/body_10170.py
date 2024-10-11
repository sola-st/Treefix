# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH: 26476
df = DataFrame(
    [["a", 1], ["a", 2], ["b", 1], ["b", 2], ["b", 3]], columns=["a", "b"]
)
result = getattr(df.groupby("a"), func)(**kwargs).sem()
expected = DataFrame(
    {"a": [np.nan] * 5, "b": [np.nan, 0.70711, np.nan, 0.70711, 0.70711]},
    index=MultiIndex.from_tuples(
        [("a", 0), ("a", 1), ("b", 2), ("b", 3), ("b", 4)], names=["a", None]
    ),
)
# GH 32262
expected = expected.drop(columns="a")
tm.assert_frame_equal(result, expected)
