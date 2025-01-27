# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
#   - assign a single value -> exp_single_cats_value
df = orig.copy()

key = (2, 0)
if indexer in [tm.loc, tm.at]:
    key = (df.index[2], df.columns[0])

# "b" is among the categories for df["cat"}]
indexer(df)[key] = "b"
tm.assert_frame_equal(df, exp_single_cats_value)

# "c" is not among the categories for df["cat"]
with pytest.raises(TypeError, match=msg1):
    indexer(df)[key] = "c"
