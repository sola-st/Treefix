# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
df = DataFrame(np.random.randn(10, 6), columns=list("abcdef"))
df_list = [df[["a", "b"]], df[["c", "d"]], df[["e", "f"]]]

joined = df_list[0].join(df_list[1:])
tm.assert_frame_equal(joined, df)

df_list = [df[["a", "b"]][:-2], df[["c", "d"]][2:], df[["e", "f"]][1:9]]

def _check_diff_index(df_list, result, exp_index):
    reindexed = [x.reindex(exp_index) for x in df_list]
    expected = reindexed[0].join(reindexed[1:])
    tm.assert_frame_equal(result, expected)

# different join types
joined = df_list[0].join(df_list[1:], how="outer")
_check_diff_index(df_list, joined, df.index)

joined = df_list[0].join(df_list[1:])
_check_diff_index(df_list, joined, df_list[0].index)

joined = df_list[0].join(df_list[1:], how="inner")
_check_diff_index(df_list, joined, df.index[2:8])

msg = "Joining multiple DataFrames only supported for joining on index"
with pytest.raises(ValueError, match=msg):
    df_list[0].join(df_list[1:], on="a")
