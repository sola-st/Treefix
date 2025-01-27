# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#49521
df = DataFrame([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
indexer = Series([0, pd.NA], dtype="Int64")
msg = "cannot convert"
with pytest.raises(ValueError, match=msg):
    df.iloc[:, indexer]
with pytest.raises(ValueError, match=msg):
    df.iloc[:, indexer.values]
