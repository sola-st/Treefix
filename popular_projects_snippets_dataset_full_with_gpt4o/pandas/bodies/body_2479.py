# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
#   - assign a complete row (mixed values) -> exp_single_row
df = orig.copy()

key = 2
if indexer is tm.loc:
    key = df.index[2]

# not categorical dtype, but "b" _is_ among the categories for df["cat"]
indexer(df)[key, :] = ["b", 2]
tm.assert_frame_equal(df, exp_single_row)

# "c" is not among the categories for df["cat"]
with pytest.raises(TypeError, match=msg1):
    indexer(df)[key, :] = ["c", 2]
