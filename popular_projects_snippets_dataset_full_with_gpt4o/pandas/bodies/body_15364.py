# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#42825 enforced in 2.0
ser = Series([1, 2, 3])
with pytest.raises(TypeError, match="as an indexer is not supported"):
    ser[key] = 1
