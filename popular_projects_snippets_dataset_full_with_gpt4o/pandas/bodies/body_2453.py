# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#46317
df = DataFrame(
    columns=["d"], index=MultiIndex.from_tuples([], names=["a", "b", "c"])
)
df.loc[(1, 2, 3)] = "foo"
expected = DataFrame(
    {"d": ["foo"]},
    index=MultiIndex.from_tuples([(1, 2, 3)], names=["a", "b", "c"]),
)
tm.assert_frame_equal(df, expected)
