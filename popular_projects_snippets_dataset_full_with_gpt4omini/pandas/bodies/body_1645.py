# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#35349
ser = Series(
    index=MultiIndex.from_tuples([("A", "0"), ("A", "1"), ("B", "0")]),
    data=[21, 22, 23],
)
msg = "Too many indexers"
with pytest.raises(IndexingError, match=msg):
    ser.loc[indexer, :]

with pytest.raises(IndexingError, match=msg):
    ser.loc[indexer, :] = 1
