# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
# GH 5344
# rename set ref_locs, and set_index was not resetting
df = DataFrame({0: ["foo", "bar"], 1: ["bah", "bas"], 2: [1, 2]})
df = df.rename(columns={0: "a"})
df = df.rename(columns={1: "b"})
df = df.set_index(["a", "b"])
df.columns = ["2001-01-01"]
expected = DataFrame(
    [[1], [2]],
    index=MultiIndex.from_tuples(
        [("foo", "bah"), ("bar", "bas")], names=["a", "b"]
    ),
    columns=["2001-01-01"],
)
tm.assert_frame_equal(df, expected)
