# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_align.py
# GH-28397
df_1 = DataFrame(
    {
        "A": np.arange(6, dtype="int64"),
        "B": Series(list("aabbca")).astype(
            pd.CategoricalDtype(list("cab"), ordered=l_ordered)
        ),
    }
).set_index("B")
df_2 = DataFrame(
    {
        "A": np.arange(5, dtype="int64"),
        "B": Series(list("babca")).astype(
            pd.CategoricalDtype(list("cab"), ordered=r_ordered)
        ),
    }
).set_index("B")

aligned_1, aligned_2 = df_1.align(df_2)
assert isinstance(aligned_1.index, expected)
assert isinstance(aligned_2.index, expected)
tm.assert_index_equal(aligned_1.index, aligned_2.index)
