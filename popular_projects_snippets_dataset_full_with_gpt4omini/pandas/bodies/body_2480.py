# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# assign a part of a column with dtype == categorical ->
# exp_parts_cats_col
df = orig.copy()

key = (slice(2, 4), 0)
if indexer is tm.loc:
    key = (slice("j", "k"), df.columns[0])

# same categories as we currently have in df["cats"]
compat = Categorical(["b", "b"], categories=["a", "b"])
indexer(df)[key] = compat
tm.assert_frame_equal(df, exp_parts_cats_col)

# categories do not match df["cat"]'s, but "b" is among them
semi_compat = Categorical(list("bb"), categories=list("abc"))
with pytest.raises(TypeError, match=msg2):
    # different categories but holdable values
    #  -> not sure if this should fail or pass
    indexer(df)[key] = semi_compat

# categories do not match df["cat"]'s, and "c" is not among them
incompat = Categorical(list("cc"), categories=list("abc"))
with pytest.raises(TypeError, match=msg2):
    # different values
    indexer(df)[key] = incompat
