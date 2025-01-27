# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# assign a part of a column with dtype != categorical -> exp_parts_cats_col
df = orig.copy()

key = (slice(2, 4), 0)
if indexer is tm.loc:
    key = (slice("j", "k"), df.columns[0])

# "b" is among the categories for df["cat"]
indexer(df)[key] = ["b", "b"]
tm.assert_frame_equal(df, exp_parts_cats_col)

# "c" not part of the categories
with pytest.raises(TypeError, match=msg1):
    indexer(df)[key] = ["c", "c"]
