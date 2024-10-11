# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
# GH 26390
df = DataFrame({"a": [1, 2, 3, 4], "b": ["a", "b", "c", "d"]})
df["c"] = pd.arrays.PandasArray(np.array([1, 2, None, 3], dtype=object))
df2 = DataFrame(
    {
        "a": [1, 2, 3, 4],
        "b": ["a", "b", "c", "d"],
        "c": pd.arrays.PandasArray(np.array([1, 2, None, 3], dtype=object)),
    }
)
assert type(df["c"]._mgr.blocks[0]) == ObjectBlock
assert type(df2["c"]._mgr.blocks[0]) == ObjectBlock
tm.assert_frame_equal(df, df2)
