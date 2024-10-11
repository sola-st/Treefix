# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_reindex.py
# GH42883
index = MultiIndex.from_tuples([(("a", None), 1), (("b", None), 2)])
index2 = MultiIndex.from_tuples([(("b", None), 2), (("a", None), 1)])
df1_dtype = pd.DataFrame([1, 2], index=index)
df2_dtype = pd.DataFrame([2, 1], index=index2)

result = df1_dtype.reindex_like(df2_dtype)
expected = df2_dtype
tm.assert_frame_equal(result, expected)
