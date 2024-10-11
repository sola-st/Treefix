# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_insert.py
# Corner case inserting with length zero doesn't raise IndexError
# GH#33573 for freq preservation
idx = timedelta_range("1 Day", periods=3)
td = idx[0]

result = idx[:0].insert(0, td)
assert result.freq == "D"

with pytest.raises(IndexError, match="loc must be an integer between"):
    result = idx[:0].insert(1, td)

with pytest.raises(IndexError, match="loc must be an integer between"):
    result = idx[:0].insert(-1, td)
