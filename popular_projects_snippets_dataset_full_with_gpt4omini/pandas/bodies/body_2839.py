# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# GH#28690
df = DataFrame(index=index_df)
result = df.reindex(index=index_res)
expected = DataFrame(index=index_exp)
tm.assert_frame_equal(result, expected)
