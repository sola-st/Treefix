# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
df = DataFrame({"a": list("abssbab")})
tm.assert_frame_equal(df.groupby("a").get_group("a"), df.iloc[[0, 5]])
# GH 13530
exp = DataFrame(index=Index(["a", "b", "s"], name="a"), columns=[])
tm.assert_frame_equal(df.groupby("a").count(), exp)
tm.assert_frame_equal(df.groupby("a").sum(), exp)

exp = df.iloc[[3, 4, 5]]
tm.assert_frame_equal(df.groupby("a").nth(1), exp)
