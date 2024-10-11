# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#917
# With a RangeIndex, an int key gives a KeyError
ser = Series([], dtype=object)
with pytest.raises(KeyError, match="-1"):
    ser[-1]
