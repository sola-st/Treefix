# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
if not len(index):
    exit()

if isinstance(index, RangeIndex):
    # tested in class
    exit()

expected = index[1:]
result = index.delete(0)
assert result.equals(expected)
assert result.name == expected.name

expected = index[:-1]
result = index.delete(-1)
assert result.equals(expected)
assert result.name == expected.name

length = len(index)
msg = f"index {length} is out of bounds for axis 0 with size {length}"
with pytest.raises(IndexError, match=msg):
    index.delete(length)
