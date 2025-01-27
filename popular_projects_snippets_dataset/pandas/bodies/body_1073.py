# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py

# GH 3738
# setting with a multi-index right hand side
arrays = [
    np.array(["bar", "bar", "baz", "qux", "qux", "bar"]),
    np.array(["one", "two", "one", "one", "two", "one"]),
    np.arange(0, 6, 1),
]

df_orig = DataFrame(
    np.random.randn(6, 3), index=arrays, columns=["A", "B", "C"]
).sort_index()

expected = df_orig.loc[["bar"]] * 2
df = df_orig.copy()
df.loc[["bar"]] *= 2
tm.assert_frame_equal(df.loc[["bar"]], expected)

# raise because these have differing levels
msg = "cannot align on a multi-index with out specifying the join levels"
with pytest.raises(TypeError, match=msg):
    df.loc["bar"] *= 2
