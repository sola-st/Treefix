# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
# GH#42825 enforced in 2.0
ser = Series([1, 2], index=MultiIndex.from_tuples([(1, 2), (3, 4)]))
with pytest.raises(TypeError, match="as an indexer is not supported"):
    ser.loc[key] = 1
